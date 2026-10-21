import unittest
import sys
import os

# Ensure current directory is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
from topic_filter import is_study_related
from ai_engine import (
    get_ai_response,
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
        quiz = generate_study_quiz(topic="Python", count=2)
        self.assertIsInstance(quiz, list)
        self.assertTrue(len(quiz) > 0)
        q1 = quiz[0]
        self.assertIn("question", q1)
        self.assertIn("options", q1)
        self.assertIn("answer", q1)
        self.assertIn("explanation", q1)
        self.assertEqual(len(q1["options"]), 4)

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
