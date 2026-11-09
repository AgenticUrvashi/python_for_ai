import unittest
import sys
import os

# Ensure current directory is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
from topic_filter import is_study_related
from ai_engine import (
    get_ai_response,
    is_study_conversation,
    safe_eval_math,
    generate_study_quiz,
    analyze_document_content,
    generate_flashcards,
    test_groq_connection
)

class TestStudyAssistant(unittest.TestCase):
    def test_study_related_queries(self):
        self.assertTrue(is_study_related("What is binary search?"))
        self.assertTrue(is_study_related("Explain photosynthesis in biology"))
        self.assertTrue(is_study_related("How to solve quadratic equations"))
        self.assertTrue(is_study_related("Write python code for bubble sort"))
        self.assertTrue(is_study_related("25 * 4 + 10"))

    def test_hinglish_study_queries(self):
        self.assertTrue(is_study_related("Recursion kya hota hai explain karo"))
        self.assertTrue(is_study_related("Python me list aur tuple me kya antar hai"))
        self.assertTrue(is_study_related("Exam ki taiyari kaise karein"))

    def test_non_study_queries(self):
        self.assertFalse(is_study_related("Who is Salman Khan?"))
        self.assertFalse(is_study_related("Tell me latest bollywood movie songs"))
        self.assertFalse(is_study_related("What is the IPL cricket score today?"))
        self.assertFalse(is_study_related("Will you marry me?"))
        self.assertFalse(is_study_related("Today weather forecast in Delhi"))

    def test_multi_turn_study_conversation_context(self):
        history = [
            {"role": "user", "content": "What is binary search?"},
            {"role": "assistant", "content": "Binary search is an algorithm for finding target in sorted array."}
        ]
        # Follow-up questions that depend on prior context should be recognized as educational
        self.assertTrue(is_study_conversation("Give an example", history))
        self.assertTrue(is_study_conversation("Why is that so?", history))
        self.assertTrue(is_study_conversation("Can you explain line 2?", history))
        self.assertTrue(is_study_conversation("How does it work?", history))

        # Explicit non-study questions must STILL be rejected even inside study history
        self.assertFalse(is_study_conversation("Who is Salman Khan?", history))
        self.assertFalse(is_study_conversation("What is the IPL cricket score today?", history))
        self.assertFalse(is_study_conversation("Will you marry me?", history))

        # Conversational farewells and pleasantries are handled by the conversational engine, not as study questions
        self.assertFalse(is_study_conversation("bye", history))
        self.assertFalse(is_study_conversation("thanks", history))

    def test_farewell_response_no_fake_study_concept(self):
        # Test standalone 'bye'
        res_standalone = get_ai_response("bye", return_details=True)
        self.assertTrue(res_standalone["is_study_related"])
        self.assertEqual(res_standalone["model_used"], "conversational-tutor")
        self.assertNotIn("Study Concept: Bye", res_standalone["answer"])
        self.assertNotIn("Sorry!", res_standalone["answer"])
        self.assertIn("Goodbye", res_standalone["answer"])

        # Test 'bye' with conversation history (the exact scenario from the bug report)
        history = [
            {"role": "user", "content": "What is binary search?"},
            {"role": "assistant", "content": "Binary search is an efficient search algorithm."}
        ]
        res_history = get_ai_response("bye", conversation_history=history, return_details=True)
        self.assertTrue(res_history["is_study_related"])
        self.assertEqual(res_history["model_used"], "conversational-tutor")
        self.assertNotIn("Study Concept: Bye", res_history["answer"])
        self.assertNotIn("Sorry!", res_history["answer"])
        self.assertIn("Goodbye", res_history["answer"])

    def test_conversational_pleasantries(self):
        # Greetings
        res_hello = get_ai_response("hello", return_details=True)
        self.assertTrue(res_hello["is_study_related"])
        self.assertEqual(res_hello["model_used"], "conversational-tutor")
        self.assertIn("Hello", res_hello["answer"])

        # Gratitude
        res_thanks = get_ai_response("thank you so much", return_details=True)
        self.assertTrue(res_thanks["is_study_related"])
        self.assertEqual(res_thanks["model_used"], "conversational-tutor")
        self.assertIn("Welcome", res_thanks["answer"])

        # Acknowledgment
        res_ok = get_ai_response("got it", return_details=True)
        self.assertTrue(res_ok["is_study_related"])
        self.assertEqual(res_ok["model_used"], "conversational-tutor")

        # Identity
        res_who = get_ai_response("who are you?", return_details=True)
        self.assertTrue(res_who["is_study_related"])
        self.assertIn("StudySync Pro", res_who["answer"])

    def test_multi_turn_ai_response_context(self):
        history = [
            {"role": "user", "content": "What is binary search in python?"},
            {"role": "assistant", "content": "Binary search is a divide and conquer algorithm with O(log n) time."}
        ]
        res = get_ai_response("What is its time complexity?", conversation_history=history, return_details=True)
        self.assertTrue(res["is_study_related"])
        self.assertNotIn("Sorry!", res["answer"])
        self.assertTrue("log" in res["answer"].lower() or "o(log n)" in res["answer"].lower() or "complexity" in res["answer"].lower())

    def test_ai_response_sorry_for_non_study(self):
        response = get_ai_response("Who won the IPL match?")
        self.assertIn("Sorry!", response)
        self.assertIn("study-related", response)

    def test_ai_response_for_math(self):
        response = get_ai_response("25 * 4")
        self.assertIn("100", response)

    def test_ai_response_for_study(self):
        response = get_ai_response("Explain binary search")
        self.assertIn("Binary Search", response)
        self.assertNotIn("Sorry!", response)

    def test_ai_response_with_details(self):
        res = get_ai_response("What is a stack in data structures?", mode="code", return_details=True)
        self.assertIsInstance(res, dict)
        self.assertIn("answer", res)
        self.assertTrue(res["is_study_related"])
        self.assertEqual(res["mode"], "code")
        self.assertTrue(len(res["model_used"]) > 0)

    def test_groq_configuration_loaded(self):
        self.assertTrue(bool(config.GROQ_API_KEY))
        self.assertEqual(config.GROQ_DEFAULT_MODEL, "qwen/qwen3.8-27b")

    def test_generate_study_quiz(self):
        quiz = generate_study_quiz(topic="Python", count=5)
        self.assertIsInstance(quiz, list)
        self.assertEqual(len(quiz), 5)
        q1 = quiz[0]
        self.assertIn("question", q1)
        self.assertIn("options", q1)
        self.assertIn("answer", q1)
        self.assertIn("explanation", q1)
        self.assertEqual(len(q1["options"]), 4)

    def test_generate_study_quiz_10_questions(self):
        quiz = generate_study_quiz(topic="Data Structures", count=10)
        self.assertIsInstance(quiz, list)
        self.assertEqual(len(quiz), 10)
        # Ensure all questions in the batch are unique
        questions_text = [q["question"] for q in quiz]
        self.assertEqual(len(questions_text), len(set(questions_text)))

    def test_test_groq_connection_success_field(self):
        res = test_groq_connection()
        self.assertIn("success", res)
        self.assertIn("status", res)

    def test_analyze_document_content(self):
        sample = "Python supports OOP principles including Inheritance, Polymorphism and Encapsulation."
        res = analyze_document_content("oop_notes.txt", sample)
        self.assertIn("summary", res)
        self.assertIn("key_takeaways", res)
        self.assertIn("suggested_questions", res)
        self.assertIn("flashcards", res)

    def test_generate_flashcards(self):
        cards = generate_flashcards("Binary Search", count=3)
        self.assertIsInstance(cards, list)
        self.assertTrue(len(cards) > 0)
        self.assertIn("front", cards[0])
        self.assertIn("back", cards[0])

if __name__ == "__main__":
    unittest.main()
