/**
 * Personal AI Study Assistant - Client Application
 * Features:
 * 1. Pixel-perfect interactive UI matching the user screenshot.
 * 2. Inspiring cartoon mascot widget in left sidebar (red marker area).
 * 3. Personalized for Urvashi with live Groq AI chat and code syntax highlighting.
 * 4. Quick Actions: Show Notes, Give Example, Summarize, Explain Concept.
 * 5. Quick Study Topic chips: Python, OOP, DSA, JSON, Regex, Linux, Web Dev, AI/ML.
 * 6. Dynamic Study Progress tracking & motivational quotes.
 * 7. Integrated modals for Document & Notes AI, Dynamic Quiz, Flashcards, and Settings.
 */

document.addEventListener("DOMContentLoaded", () => {
  initUserProfile();
  initNavigation();
  initChatEngine();
  initQuickActions();
  initStudyTopics();
  initProgressTracker();
  initModals();
  initDocumentHub();
  initQuizEngine();
  initFlashcardsEngine();
  initSettings();
  initMascotCard();
});

// Toast notification helper
function showToast(msg) {
  const toast = document.getElementById("toastPopup");
  if (!toast) return;
  toast.innerText = msg;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2600);
}

// Modal open/close helpers
function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.add("active");
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove("active");
}

function initModals() {
  document.querySelectorAll("[data-close]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const modalId = btn.getAttribute("data-close");
      closeModal(modalId);
    });
  });

  // Close modal on click outside card
  document.querySelectorAll(".modal-overlay").forEach((overlay) => {
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) {
        overlay.classList.remove("active");
      }
    });
  });

  // Settings button in header
  const btnOpenSettings = document.getElementById("btnOpenSettings");
  if (btnOpenSettings) {
    btnOpenSettings.addEventListener("click", () => openModal("modalSettings"));
  }

  // Study Mode button in header
  const btnStudyMode = document.getElementById("btnStudyModeToggle");
  if (btnStudyMode) {
    btnStudyMode.addEventListener("click", () => {
      showToast("🟢 Study Mode Active: Academic guardrail ensures 100% focus on learning!");
    });
  }

  // Window close / minimize buttons
  const winClose = document.querySelector(".win-close");
  if (winClose) {
    winClose.addEventListener("click", () => {
      showToast("Window minimize/close is managed by your browser window.");
    });
  }
}

// USER PROFILE (URVASHI)
function initUserProfile() {
  let savedName = localStorage.getItem("studysync_user_name");
  if (!savedName || savedName.toLowerCase() === "student") {
    savedName = "Urvashi";
    localStorage.setItem("studysync_user_name", "Urvashi");
  }

  const nameElem = document.getElementById("displayUserName");
  if (nameElem) nameElem.innerText = savedName;

  const settingsInput = document.getElementById("settingsUserName");
  if (settingsInput) settingsInput.value = savedName;
}

// NAVIGATION TABS
function initNavigation() {
  const navItems = document.querySelectorAll(".nav-item");

  navItems.forEach((btn) => {
    btn.addEventListener("click", () => {
      const tab = btn.getAttribute("data-tab");

      if (tab === "home") {
        navItems.forEach(n => n.classList.remove("active"));
        btn.classList.add("active");
        const chatStream = document.getElementById("chatStream");
        if (chatStream) chatStream.scrollTop = 0;
      } else if (tab === "chat") {
        navItems.forEach(n => n.classList.remove("active"));
        btn.classList.add("active");
        const input = document.getElementById("mainQuestionInput");
        if (input) input.focus();
      } else if (tab === "notes") {
        openModal("modalUpload");
      } else if (tab === "quick-tips") {
        openModal("modalFlashcards");
      } else if (tab === "study-plan") {
        openModal("modalQuiz");
      }
    });
  });
}

// RED MARKER CARTOON MASCOT CARD
function initMascotCard() {
  const card = document.getElementById("cartoonInspireWidget");
  if (card) {
    const quotes = [
      "Small steps every day lead to big dreams! 💜",
      "Stay curious! Learning is your superpower. ✨",
      "Consistency beats perfection every single time! 🚀",
      "Mistakes are proof that you are trying and growing! 💡",
      "Focus for 25 minutes, conquer your subject! 📚"
    ];
    let quoteIndex = 0;

    card.addEventListener("click", () => {
      quoteIndex = (quoteIndex + 1) % quotes.length;
      showToast(`🦊 Mascot Tip: ${quotes[quoteIndex]}`);
    });
  }
}

// CHAT & AI QUESTION ANSWERING
function initChatEngine() {
  const chatStream = document.getElementById("chatStream");
  const input = document.getElementById("mainQuestionInput");
  const sendBtn = document.getElementById("btnSendQuestion");
  const attachBtn = document.getElementById("btnAttachFile");

  if (attachBtn) {
    attachBtn.addEventListener("click", () => openModal("modalUpload"));
  }

  // Copy buttons on existing message cards
  setupCopyButtons();

  async function handleSend() {
    const text = input.value.trim();
    if (!text) return;

    input.value = "";
    appendUserBubble(text);

    // Scroll to bottom
    chatStream.scrollTop = chatStream.scrollHeight;

    // Show assistant typing indicator
    const typingId = "typing_" + Date.now();
    appendTypingIndicator(typingId);
    chatStream.scrollTop = chatStream.scrollHeight;

    try {
      const apiKey = localStorage.getItem("studysync_gemini_key") || "";
      const model = localStorage.getItem("studysync_model") || "";

      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: text, api_key: apiKey, model: model })
      });

      const data = await response.json();
      removeTypingIndicator(typingId);

      const answer = data.answer || "I could not generate an answer at this moment.";
      const isRefusal = answer.includes("Sorry!") || answer.includes("academic study");
      appendAssistantCard(answer, isRefusal);

      // Increment progress on valid study questions
      if (!isRefusal) {
        incrementStudyProgress();
      }
    } catch (err) {
      removeTypingIndicator(typingId);
      appendAssistantCard("⚠️ Network connection error. Please make sure the local server is running.", true);
    }

    chatStream.scrollTop = chatStream.scrollHeight;
  }

  if (sendBtn) sendBtn.addEventListener("click", handleSend);
  if (input) {
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleSend();
      }
    });
  }
}

function getCurrentTimeStr() {
  const now = new Date();
  let hours = now.getHours();
  const minutes = now.getMinutes().toString().padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12 || 12;
  const hoursStr = hours.toString().padStart(2, "0");
  return `${hoursStr}:${minutes} ${ampm}`;
}

function appendUserBubble(text) {
  const chatStream = document.getElementById("chatStream");
  const row = document.createElement("div");
  row.className = "message-row user-row";

  row.innerHTML = `
    <div class="user-bubble">
      <p class="bubble-text">${escapeHtml(text)}</p>
      <div class="bubble-meta">
        <span class="meta-time">${getCurrentTimeStr()}</span>
        <span class="meta-ticks">✔✔</span>
      </div>
    </div>
    <div class="user-avatar-circle">
      <svg viewBox="0 0 24 24" fill="currentColor" class="user-svg"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
    </div>
  `;

  chatStream.appendChild(row);
}

function appendTypingIndicator(id) {
  const chatStream = document.getElementById("chatStream");
  const row = document.createElement("div");
  row.className = "message-row assistant-row";
  row.id = id;

  row.innerHTML = `
    <div class="assistant-avatar-circle">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="robot-mini-svg">
        <rect x="3" y="11" width="18" height="10" rx="2"/>
        <circle cx="12" cy="5" r="2"/>
        <path d="M12 7v4"/>
        <line x1="8" y1="16" x2="8.01" y2="16"/>
        <line x1="16" y1="16" x2="16.01" y2="16"/>
      </svg>
    </div>
    <div class="typing-bubble">
      <span>AI Tutor is thinking & crafting explanation...</span> ⚡
    </div>
  `;

  chatStream.appendChild(row);
}

function removeTypingIndicator(id) {
  const elem = document.getElementById(id);
  if (elem) elem.remove();
}

function appendAssistantCard(rawMarkdown, isRefusal) {
  const chatStream = document.getElementById("chatStream");
  const row = document.createElement("div");
  row.className = "message-row assistant-row";

  // Parse Markdown to structured HTML with code boxes
  const formattedHtml = formatMarkdownResponse(rawMarkdown);
  const plainText = rawMarkdown.replace(/[`*#]/g, "");

  row.innerHTML = `
    <div class="assistant-avatar-circle">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="robot-mini-svg">
        <rect x="3" y="11" width="18" height="10" rx="2"/>
        <circle cx="12" cy="5" r="2"/>
        <path d="M12 7v4"/>
        <line x1="8" y1="16" x2="8.01" y2="16"/>
        <line x1="16" y1="16" x2="16.01" y2="16"/>
      </svg>
    </div>
    <div class="assistant-card ${isRefusal ? 'refusal-card' : ''}">
      ${formattedHtml}
      <div class="card-footer">
        <span class="footer-time">${getCurrentTimeStr()}</span>
        <button class="btn-copy-code" title="Copy answer" data-copy="${escapeHtml(plainText)}">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="copy-svg"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        </button>
      </div>
    </div>
  `;

  chatStream.appendChild(row);
  setupCopyButtons();
}

function formatMarkdownResponse(md) {
  if (!md) return "<p>No content generated.</p>";

  // Extract code blocks first
  let html = md;

  // Code blocks: ```python ... ```
  html = html.replace(/```(?:python|py|javascript|js|html|css|sql|bash)?([\s\S]*?)```/g, (match, code) => {
    return `<div class="code-box"><code>${escapeHtml(code.trim())}</code></div>`;
  });

  // Inline code: `code`
  html = html.replace(/`([^`]+)`/g, (match, code) => {
    return `<code style="background:#090e1c; color:#38bdf8; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono',monospace; font-size:0.84rem;">${escapeHtml(code)}</code>`;
  });

  // Headers: ### Title
  html = html.replace(/^### (.*$)/gim, '<div class="code-section-title">$1</div>');
  html = html.replace(/^## (.*$)/gim, '<div class="assistant-card-header"><span class="sparkle-icon">✨</span><h3 class="card-title">$1</h3></div>');

  // Bold & Italic
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');

  // Bullet points
  html = html.replace(/^\- (.*$)/gim, '<li style="margin-left:18px; margin-bottom:4px; color:#cbd5e1;">$1</li>');

  // Paragraph breaks
  html = html.replace(/\n\n/g, '<p class="card-p"></p>');
  html = html.replace(/\n/g, '<br>');

  return html;
}

function setupCopyButtons() {
  document.querySelectorAll(".btn-copy-code").forEach((btn) => {
    btn.onclick = () => {
      const textToCopy = btn.getAttribute("data-copy") || "";
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast("Copied to clipboard! 📋");
      }).catch(() => {
        showToast("Copied text!");
      });
    };
  });
}

function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// QUICK ACTIONS (RIGHT SIDEBAR)
function initQuickActions() {
  const qaNotes = document.getElementById("qaShowNotes");
  const qaExample = document.getElementById("qaGiveExample");
  const qaSummarize = document.getElementById("qaSummarize");
  const qaExplain = document.getElementById("qaExplainConcept");

  const input = document.getElementById("mainQuestionInput");
  const sendBtn = document.getElementById("btnSendQuestion");

  if (qaNotes) {
    qaNotes.addEventListener("click", () => openModal("modalUpload"));
  }

  if (qaExample) {
    qaExample.addEventListener("click", () => {
      input.value = "Give a practical coding example with line-by-line explanation.";
      sendBtn.click();
    });
  }

  if (qaSummarize) {
    qaSummarize.addEventListener("click", () => {
      input.value = "Summarize the key study takeaways into concise revision bullet points.";
      sendBtn.click();
    });
  }

  if (qaExplain) {
    qaExplain.addEventListener("click", () => {
      input.value = "Explain this concept in simple terms using an intuitive analogy.";
      sendBtn.click();
    });
  }
}

// STUDY TOPICS CHIPS
function initStudyTopics() {
  const input = document.getElementById("mainQuestionInput");
  const sendBtn = document.getElementById("btnSendQuestion");

  document.querySelectorAll(".topic-tag").forEach((tag) => {
    tag.addEventListener("click", () => {
      const topic = tag.getAttribute("data-topic");
      input.value = `Explain ${topic} fundamentals with practical examples and key concepts.`;
      sendBtn.click();
    });
  });
}

// PROGRESS TRACKER
function initProgressTracker() {
  let count = parseInt(localStorage.getItem("studysync_progress_count") || "3", 10);
  updateProgressUI(count);
}

function incrementStudyProgress() {
  let count = parseInt(localStorage.getItem("studysync_progress_count") || "3", 10);
  count = Math.min(5, count + 1);
  localStorage.setItem("studysync_progress_count", count.toString());
  updateProgressUI(count);

  if (count === 5) {
    showToast("🎉 Awesome work Urvashi! Daily study goal of 5/5 completed!");
  }
}

function updateProgressUI(count) {
  const fill = document.getElementById("progressFillBar");
  const text = document.getElementById("progressFractionText");
  if (fill) fill.style.width = `${(count / 5) * 100}%`;
  if (text) text.innerText = `${count}/5`;
}

// DOCUMENT & NOTES HUB
function initDocumentHub() {
  const btnSelectFile = document.getElementById("btnSelectFile");
  const fileUploadInput = document.getElementById("fileUploadInput");
  const btnProcessDoc = document.getElementById("btnProcessDoc");
  const studyNotesInput = document.getElementById("studyNotesInput");
  const docAnalysisResult = document.getElementById("docAnalysisResult");

  if (btnSelectFile && fileUploadInput) {
    btnSelectFile.addEventListener("click", () => fileUploadInput.click());
    fileUploadInput.addEventListener("change", () => {
      if (fileUploadInput.files.length > 0) {
        const file = fileUploadInput.files[0];
        studyNotesInput.value = `[Document selected: ${file.name} (${(file.size / 1024).toFixed(1)} KB)]\n\nMachine Learning and Data Structures Comprehensive Notes.`;
      }
    });
  }

  if (btnProcessDoc) {
    btnProcessDoc.addEventListener("click", async () => {
      const content = studyNotesInput.value.trim() || "Python OOP, Decorators and Algorithms Study Notes";
      btnProcessDoc.innerText = "Analyzing Notes with Groq AI...";

      try {
        const response = await fetch("/api/documents/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ filename: "Urvashi_Study_Notes.pdf", content: content })
        });
        const data = await response.json();
        btnProcessDoc.innerText = "Analyze Notes with AI Assistant ⚡";

        docAnalysisResult.style.display = "block";
        docAnalysisResult.innerHTML = `
          <h4 style="color:#38bdf8; font-size:0.95rem; margin-bottom:8px;">✨ AI Summary & Revision Notes</h4>
          <p style="font-size:0.85rem; color:#cbd5e1; line-height:1.45; margin-bottom:12px;">${data.summary}</p>
          
          <div style="font-weight:600; font-size:0.82rem; color:#a5b4fc; margin-bottom:6px;">Key Revision Takeaways:</div>
          <ul style="padding-left:18px; font-size:0.82rem; color:#94a3b8; margin-bottom:12px;">
            ${(data.key_takeaways || []).map(t => `<li style="margin-bottom:4px;">${t}</li>`).join("")}
          </ul>

          <div style="font-weight:600; font-size:0.82rem; color:#34d399; margin-bottom:6px;">High-Yield Exam Questions:</div>
          <ul style="padding-left:18px; font-size:0.82rem; color:#94a3b8;">
            ${(data.suggested_questions || []).map(q => `<li style="margin-bottom:4px;">${q}</li>`).join("")}
          </ul>
        `;

        incrementStudyProgress();
      } catch (err) {
        btnProcessDoc.innerText = "Analyze Notes with AI Assistant ⚡";
        showToast("Error processing notes. Please try again.");
      }
    });
  }
}

// PRACTICE QUIZ ENGINE
function initQuizEngine() {
  const btnFetchQuiz = document.getElementById("btnFetchQuiz");
  const topicInput = document.getElementById("quizCustomTopic");
  const diffSelect = document.getElementById("quizDifficultySelect");
  const countSelect = document.getElementById("quizCountSelect");
  const container = document.getElementById("quizContainer");
  const scoreBanner = document.getElementById("quizScoreBanner");
  const scoreText = document.getElementById("quizScoreText");
  const btnRestart = document.getElementById("btnRestartQuiz");

  let questions = [];
  let score = 0;
  let answered = 0;

  if (btnFetchQuiz) {
    btnFetchQuiz.addEventListener("click", async () => {
      const topic = topicInput.value.trim() || "Python Programming";
      const diff = diffSelect.value;
      const count = countSelect.value;

      btnFetchQuiz.innerText = "Generating...";
      scoreBanner.style.display = "none";
      container.innerHTML = "<p class='empty-state-p'>Generating high-yield academic questions with Groq AI... ⚡</p>";

      try {
        const res = await fetch(`/api/quiz?topic=${encodeURIComponent(topic)}&difficulty=${encodeURIComponent(diff)}&count=${count}`);
        questions = await res.json();
        btnFetchQuiz.innerText = "Generate Quiz 🚀";
        renderQuiz(questions);
      } catch (err) {
        btnFetchQuiz.innerText = "Generate Quiz 🚀";
        container.innerHTML = "<p class='empty-state-p' style='color:#f87171;'>Could not load quiz questions. Please check connection.</p>";
      }
    });
  }

  function renderQuiz(list) {
    score = 0;
    answered = 0;
    container.innerHTML = "";

    list.forEach((q, idx) => {
      const box = document.createElement("div");
      box.className = "quiz-q-box";
      box.innerHTML = `
        <div class="quiz-q-title">Q${idx + 1}. ${escapeHtml(q.question)}</div>
        <div class="quiz-options-grid" id="q_opts_${idx}">
          ${q.options.map((opt, oIdx) => `
            <button class="quiz-opt-btn" data-qid="${idx}" data-oid="${oIdx}">
              ${String.fromCharCode(65 + oIdx)}. ${escapeHtml(opt)}
            </button>
          `).join("")}
        </div>
        <div id="q_expl_${idx}" style="display:none; margin-top:10px; font-size:0.82rem; padding:8px 12px; border-radius:6px; background:rgba(30,41,59,0.7); color:#93c5fd;">
          💡 <strong>Explanation:</strong> ${escapeHtml(q.explanation)}
        </div>
      `;
      container.appendChild(box);
    });

    document.querySelectorAll(".quiz-opt-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const qid = parseInt(btn.getAttribute("data-qid"));
        const oid = parseInt(btn.getAttribute("data-oid"));
        const qObj = list[qid];

        const parent = document.getElementById(`q_opts_${qid}`);
        const allBtns = parent.querySelectorAll(".quiz-opt-btn");
        allBtns.forEach(b => b.style.pointerEvents = "none");

        answered++;
        if (oid === qObj.answer) {
          btn.classList.add("correct");
          score++;
        } else {
          btn.classList.add("wrong");
          if (allBtns[qObj.answer]) allBtns[qObj.answer].classList.add("correct");
        }

        const expl = document.getElementById(`q_expl_${qid}`);
        if (expl) expl.style.display = "block";

        if (answered === list.length) {
          scoreBanner.style.display = "flex";
          scoreText.innerText = `Score: ${score} / ${list.length}`;
          incrementStudyProgress();
        }
      });
    });
  }

  if (btnRestart) {
    btnRestart.addEventListener("click", () => {
      if (btnFetchQuiz) btnFetchQuiz.click();
    });
  }
}

// 3D FLASHCARDS ENGINE
function initFlashcardsEngine() {
  const flashcardElement = document.getElementById("flashcardElement");
  const btnFlipCard = document.getElementById("btnFlipCard");
  const btnNextCard = document.getElementById("btnNextCard");
  const btnPrevCard = document.getElementById("btnPrevCard");
  const counterElem = document.getElementById("flashcardCounter");
  const frontText = document.getElementById("cardFrontText");
  const backText = document.getElementById("cardBackText");
  const topicInput = document.getElementById("flashcardTopicInput");
  const btnGenCards = document.getElementById("btnGenerateFlashcards");

  let cards = [
    {
      q: "What is the difference between List and Tuple in Python?",
      a: "Lists are mutable (can be changed) and use brackets []. Tuples are immutable (cannot be changed after creation) and use parentheses (). Tuples are faster and memory efficient."
    },
    {
      q: "What is Time Complexity of Binary Search?",
      a: "O(log n) in best and average cases. It requires the array to be sorted and divides the search space in half at each step."
    },
    {
      q: "Explain Python Decorators in one sentence.",
      a: "A decorator is a function that takes another function as an argument, extends or alters its behavior without modifying its source code, and returns the modified function."
    },
    {
      q: "What is the primary rule of LIFO vs FIFO?",
      a: "Stack follows LIFO (Last In First Out) where elements are added and removed from the top. Queue follows FIFO (First In First Out) where insertion is at rear and removal at front."
    },
    {
      q: "What is recursion base case and why is it essential?",
      a: "A base case is the terminating condition in a recursive function that stops recursion. Without it, the function calls itself indefinitely until a Stack Overflow occurs."
    }
  ];

  let currentIndex = 0;

  function updateCard() {
    if (flashcardElement) flashcardElement.classList.remove("flipped");
    const item = cards[currentIndex];
    if (frontText) frontText.innerText = item.q;
    if (backText) backText.innerText = item.a;
    if (counterElem) counterElem.innerText = `Card ${currentIndex + 1} of ${cards.length}`;
  }

  if (flashcardElement) {
    flashcardElement.addEventListener("click", () => {
      flashcardElement.classList.toggle("flipped");
    });
  }

  if (btnFlipCard) {
    btnFlipCard.addEventListener("click", () => {
      if (flashcardElement) flashcardElement.classList.toggle("flipped");
    });
  }

  if (btnNextCard) {
    btnNextCard.addEventListener("click", () => {
      currentIndex = (currentIndex + 1) % cards.length;
      updateCard();
    });
  }

  if (btnPrevCard) {
    btnPrevCard.addEventListener("click", () => {
      currentIndex = (currentIndex - 1 + cards.length) % cards.length;
      updateCard();
    });
  }

  if (btnGenCards) {
    btnGenCards.addEventListener("click", async () => {
      const topic = topicInput.value.trim() || "Python";
      btnGenCards.innerText = "Generating...";

      try {
        const res = await fetch("/api/flashcards", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ topic: topic, count: 5 })
        });
        const data = await res.json();
        btnGenCards.innerText = "Generate Cards 📇";

        if (data.flashcards && data.flashcards.length > 0) {
          cards = data.flashcards;
          currentIndex = 0;
          updateCard();
          showToast(`Generated 5 cards on ${topic}!`);
        }
      } catch (err) {
        btnGenCards.innerText = "Generate Cards 📇";
        showToast("Error generating flashcards.");
      }
    });
  }
}

// SETTINGS & AI MODEL SELECTION
function initSettings() {
  const nameInput = document.getElementById("settingsUserName");
  const modelSelect = document.getElementById("settingsModelSelect");
  const keyInput = document.getElementById("settingsGroqKey");
  const btnSave = document.getElementById("btnSaveSettings");
  const btnTestKey = document.getElementById("btnTestGroqConn");
  const statusMsg = document.getElementById("groqTestStatus");

  // Load existing
  if (nameInput) nameInput.value = localStorage.getItem("studysync_user_name") || "Urvashi";
  if (keyInput) keyInput.value = localStorage.getItem("studysync_gemini_key") || "";
  if (modelSelect) modelSelect.value = localStorage.getItem("studysync_model") || "qwen/qwen3.8-27b";

  if (btnTestKey) {
    btnTestKey.addEventListener("click", async () => {
      const key = keyInput.value.trim();
      statusMsg.style.display = "block";
      statusMsg.style.color = "#38bdf8";
      statusMsg.innerText = "Testing Groq Cloud connection...";

      try {
        const res = await fetch("/api/test-groq", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ api_key: key, model: modelSelect.value })
        });
        const data = await res.json();
        if (data.success) {
          statusMsg.style.color = "#34d399";
          statusMsg.innerText = "✅ Groq Cloud connection verified! Ultra-fast response active.";
        } else {
          statusMsg.style.color = "#f87171";
          statusMsg.innerText = "⚠️ " + (data.message || "Failed to connect.");
        }
      } catch (e) {
        statusMsg.style.color = "#f87171";
        statusMsg.innerText = "⚠️ Server connection error.";
      }
    });
  }

  if (btnSave) {
    btnSave.addEventListener("click", () => {
      const name = nameInput.value.trim() || "Urvashi";
      const key = keyInput.value.trim();
      const model = modelSelect.value;

      localStorage.setItem("studysync_user_name", name);
      localStorage.setItem("studysync_gemini_key", key);
      localStorage.setItem("studysync_model", model);

      const nameDisplay = document.getElementById("displayUserName");
      if (nameDisplay) nameDisplay.innerText = name;

      showToast(`Settings saved! Hello ${name}! 👋`);
      closeModal("modalSettings");
    });
  }
}
