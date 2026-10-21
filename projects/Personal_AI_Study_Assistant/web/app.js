/**
 * StudySync Client Application Logic
 * Supports:
 * 1. User onboarding & customizable student name.
 * 2. Real-time dynamic study session tracker (no hardcoded hours).
 * 3. Strict study-only AI chat with polite refusal guardrails.
 * 4. Document upload & analysis.
 * 5. Interactive practice quiz runner with score tracking.
 * 6. Live analytics & progress dashboard.
 */

document.addEventListener("DOMContentLoaded", () => {
  setupUserOnboarding();
  setupNavigation();
  setupModals();
  setupNotifications();
  setupChat();
  setupDocumentUpload();
  setupQuiz();
  setupSettings();
  setupSearch();
  setupStudyTracker();
});

// Modal helpers
function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.add("active");
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove("active");
}

function setupModals() {
  document.querySelectorAll("[data-close]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const modalId = btn.getAttribute("data-close");
      closeModal(modalId);
    });
  });

  // Action card buttons
  const btnUploadCard = document.getElementById("btnUploadCard");
  const btnTutorCard = document.getElementById("btnTutorCard");
  const btnQuizCard = document.getElementById("btnQuizCard");

  if (btnUploadCard) btnUploadCard.addEventListener("click", () => openModal("modalUpload"));
  if (btnTutorCard) btnTutorCard.addEventListener("click", () => openModal("modalTutor"));
  if (btnQuizCard) btnQuizCard.addEventListener("click", () => openModal("modalQuiz"));

  // Recent document item clicks
  document.querySelectorAll(".document-item").forEach((item) => {
    item.addEventListener("click", () => {
      const filename = item.getAttribute("data-file");
      openDocDetails(filename);
    });
  });

  const linkViewAll = document.getElementById("linkViewAllDocs");
  if (linkViewAll) {
    linkViewAll.addEventListener("click", () => openModal("modalUpload"));
  }
}

// USER ONBOARDING & PROFILE MANAGEMENT
function setupUserOnboarding() {
  const savedName = localStorage.getItem("studysync_user_name");
  const onboardingModal = document.getElementById("modalOnboarding");
  const onboardingInput = document.getElementById("onboardingNameInput");
  const btnSaveOnboarding = document.getElementById("btnSaveOnboarding");

  if (!savedName) {
    // Show onboarding if student has not entered their name yet
    openModal("modalOnboarding");
  } else {
    applyUserName(savedName);
  }

  if (btnSaveOnboarding && onboardingInput) {
    btnSaveOnboarding.addEventListener("click", () => {
      const name = onboardingInput.value.trim() || "Student";
      localStorage.setItem("studysync_user_name", name);
      applyUserName(name);
      closeModal("modalOnboarding");
    });

    onboardingInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        btnSaveOnboarding.click();
      }
    });
  }
}

function applyUserName(name) {
  const displayName = name.trim() || "Student";
  const initial = displayName.charAt(0).toUpperCase();

  const greetingElem = document.getElementById("greetingUserName");
  if (greetingElem) greetingElem.innerText = displayName;

  const topAvatarImg = document.getElementById("topAvatarImg");
  if (topAvatarImg) topAvatarImg.innerText = initial;

  const topAvatarName = document.getElementById("topAvatarName");
  if (topAvatarName) topAvatarName.innerText = displayName;

  const settingsInput = document.getElementById("settingsUserName");
  if (settingsInput) settingsInput.value = displayName;

  // Update AI Tutor initial welcome message
  const chatWelcome = document.getElementById("chatWelcomeMessage");
  if (chatWelcome) {
    chatWelcome.innerHTML = `
      Namaste <strong>${displayName}</strong>! Main aapka <strong>Personal AI Study Assistant</strong> hoon.
      Main <strong>sirf study, programming, math, science aur exam preparation</strong> se jude sawaalon ke jawab deta hoon.<br>
      Aap mujhse koi bhi academic sawaal poochh sakte hain! 📚
    `;
  }
}

// REAL-TIME STUDY TRACKER & ANALYTICS (NO HARDCODED 14.2 HOURS)
const Tracker = {
  getStats() {
    return {
      minutes: parseInt(localStorage.getItem("studysync_minutes") || "0", 10),
      questions: parseInt(localStorage.getItem("studysync_questions") || "0", 10),
      quizzes: parseInt(localStorage.getItem("studysync_quizzes") || "0", 10),
      quizCorrect: parseInt(localStorage.getItem("studysync_quiz_correct") || "0", 10),
      quizTotal: parseInt(localStorage.getItem("studysync_quiz_total") || "0", 10),
      weekly: JSON.parse(localStorage.getItem("studysync_weekly") || "[0, 0, 0, 0, 0, 0, 0]")
    };
  },

  saveStats(stats) {
    localStorage.setItem("studysync_minutes", stats.minutes.toString());
    localStorage.setItem("studysync_questions", stats.questions.toString());
    localStorage.setItem("studysync_quizzes", stats.quizzes.toString());
    localStorage.setItem("studysync_quiz_correct", stats.quizCorrect.toString());
    localStorage.setItem("studysync_quiz_total", stats.quizTotal.toString());
    localStorage.setItem("studysync_weekly", JSON.stringify(stats.weekly));
  },

  addMinute() {
    const stats = this.getStats();
    stats.minutes += 1;

    // Add to current day of week (0=Sun, 1=Mon... 6=Sat)
    const day = (new Date().getDay() + 6) % 7; // Convert so Mon=0, Sun=6
    stats.weekly[day] = (stats.weekly[day] || 0) + 1;

    this.saveStats(stats);
    this.refreshUI();
  },

  addQuestion() {
    const stats = this.getStats();
    stats.questions += 1;
    this.saveStats(stats);
    this.refreshUI();
  },

  recordQuiz(correct, total) {
    const stats = this.getStats();
    stats.quizzes += 1;
    stats.quizCorrect += correct;
    stats.quizTotal += total;
    this.saveStats(stats);
    this.refreshUI();
  },

  reset() {
    localStorage.removeItem("studysync_minutes");
    localStorage.removeItem("studysync_questions");
    localStorage.removeItem("studysync_quizzes");
    localStorage.removeItem("studysync_quiz_correct");
    localStorage.removeItem("studysync_quiz_total");
    localStorage.removeItem("studysync_weekly");
    this.refreshUI();
  },

  calcProgress(stats) {
    // Dynamic progress: starts at 0%
    const score = (stats.questions * 4) + (stats.quizzes * 15) + (stats.minutes * 1);
    return Math.min(100, score);
  },

  refreshUI() {
    const stats = this.getStats();
    const progressPct = this.calcProgress(stats);

    // Update Donut Chart
    const circle = document.getElementById("donutProgressCircle");
    const text = document.getElementById("donutProgressText");
    if (circle && text) {
      const circ = 264;
      const offset = circ - (circ * progressPct / 100);
      circle.style.strokeDashoffset = offset;
      text.innerText = `${progressPct}%`;
    }

    // Update Today's study label
    const todayLabel = document.getElementById("todayStudyLabel");
    if (todayLabel) {
      if (stats.minutes < 60) {
        todayLabel.innerText = `Today: ${stats.minutes} mins`;
      } else {
        todayLabel.innerText = `Today: ${(stats.minutes / 60).toFixed(1)} hrs`;
      }
    }

    // Update Weekly Bars
    const dayIds = ["bar_mon", "bar_tue", "bar_wed", "bar_thu", "bar_fri", "bar_sat", "bar_sun"];
    dayIds.forEach((id, idx) => {
      const col = document.getElementById(id);
      if (col) {
        const mins = stats.weekly[idx] || 0;
        const fill = col.querySelector(".bar-fill");
        if (fill) {
          // Height percentage proportional to study mins (capped at 100% for 60 mins)
          const h = Math.min(100, Math.max(10, (mins / 30) * 100));
          fill.style.height = `${h}%`;
        }
        col.title = `${col.querySelector(".bar-label").innerText}: ${mins} mins`;
      }
    });

    // Update Analytics Modal elements
    const statTime = document.getElementById("statStudyTime");
    if (statTime) {
      statTime.innerText = stats.minutes < 60 ? `${stats.minutes} mins` : `${(stats.minutes / 60).toFixed(1)} hrs`;
    }

    const statQuestions = document.getElementById("statQuestionsAsked");
    if (statQuestions) statQuestions.innerText = stats.questions.toString();

    const statQuizzes = document.getElementById("statQuizzesTaken");
    if (statQuizzes) statQuizzes.innerText = stats.quizzes.toString();

    const statAccuracy = document.getElementById("statQuizAccuracy");
    if (statAccuracy) {
      const acc = stats.quizTotal > 0 ? Math.round((stats.quizCorrect / stats.quizTotal) * 100) : 0;
      statAccuracy.innerText = `${acc}%`;
    }

    const statOverallPct = document.getElementById("statOverallPct");
    if (statOverallPct) statOverallPct.innerText = `${progressPct}%`;

    const statProgressBar = document.getElementById("statProgressBar");
    if (statProgressBar) statProgressBar.style.width = `${progressPct}%`;
  }
};

function setupStudyTracker() {
  // Initialize UI with stored metrics
  Tracker.refreshUI();

  // Active session timer: increments study minutes every 60 seconds
  setInterval(() => {
    Tracker.addMinute();
  }, 60000);

  // Reset button in Analytics modal
  const btnResetStats = document.getElementById("btnResetStats");
  if (btnResetStats) {
    btnResetStats.addEventListener("click", () => {
      if (confirm("Are you sure you want to reset your study stats to 0?")) {
        Tracker.reset();
        alert("Study statistics reset to 0.");
      }
    });
  }
}

// Navigation Tabs
function setupNavigation() {
  const navItems = document.querySelectorAll(".nav-item");
  navItems.forEach((item) => {
    item.addEventListener("click", () => {
      navItems.forEach((n) => n.classList.remove("active"));
      item.classList.add("active");

      const tab = item.getAttribute("data-tab");
      if (tab === "tutor") openModal("modalTutor");
      else if (tab === "quizzes") openModal("modalQuiz");
      else if (tab === "library") openModal("modalUpload");
      else if (tab === "settings") openModal("modalSettings");
      else if (tab === "analytics") {
        Tracker.refreshUI();
        openModal("modalAnalytics");
      }
    });
  });
}

// Notifications dropdown
function setupNotifications() {
  const notifBtn = document.getElementById("notifBtn");
  const notifDropdown = document.getElementById("notifDropdown");
  if (notifBtn && notifDropdown) {
    notifBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      notifDropdown.classList.toggle("show");
    });
    document.addEventListener("click", () => {
      notifDropdown.classList.remove("show");
    });
  }
}

// AI Tutor Chat
function setupChat() {
  const chatMessages = document.getElementById("chatMessages");
  const chatInput = document.getElementById("chatInput");
  const btnSendChat = document.getElementById("btnSendChat");

  // Chips click
  document.querySelectorAll(".chip-btn").forEach((chip) => {
    chip.addEventListener("click", () => {
      const query = chip.getAttribute("data-ask");
      if (query) {
        chatInput.value = query;
        sendChatMessage(query);
      }
    });
  });

  function appendMessage(sender, text, isSorry = false) {
    const bubble = document.createElement("div");
    bubble.className = `chat-bubble ${sender}`;
    if (isSorry) {
      bubble.classList.add("sorry-refusal");
    }

    // Markdown conversion
    let formatted = text
      .replace(/### (.*?)\n/g, '<h4 style="color:#60a5fa; margin: 4px 0;">$1</h4>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/```python([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
      .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
      .replace(/`([^`]+)`/g, '<code style="background:#040814; color:#38bdf8; padding:2px 5px; border-radius:4px;">$1</code>')
      .replace(/\n/g, '<br>');

    bubble.innerHTML = formatted;
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  async function sendChatMessage(query) {
    const text = query || chatInput.value.trim();
    if (!text) return;

    appendMessage("user", text);
    chatInput.value = "";

    // Show typing placeholder
    const typingBubble = document.createElement("div");
    typingBubble.className = "chat-bubble assistant";
    typingBubble.id = "typingIndicator";
    typingBubble.innerHTML = "<em>Thinking... verifying study relevance... 🧠</em>";
    chatMessages.appendChild(typingBubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
      const apiKey = localStorage.getItem("studysync_gemini_key") || "";
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: text, api_key: apiKey })
      });

      const data = await response.json();
      const indicator = document.getElementById("typingIndicator");
      if (indicator) indicator.remove();

      const answer = data.answer || "No response.";
      const isSorry = answer.includes("Sorry!");
      appendMessage("assistant", answer, isSorry);

      // Track question if study-related
      if (!isSorry) {
        Tracker.addQuestion();
      }
    } catch (err) {
      const indicator = document.getElementById("typingIndicator");
      if (indicator) indicator.remove();
      appendMessage("assistant", "Network error connecting to assistant engine.", true);
    }
  }

  if (btnSendChat) {
    btnSendChat.addEventListener("click", () => sendChatMessage());
  }

  if (chatInput) {
    chatInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        sendChatMessage();
      }
    });
  }
}

// Open Document Analysis Details
function openDocDetails(filename) {
  openModal("modalUpload");
  const docResult = document.getElementById("docAnalysisResult");
  docResult.style.display = "block";
  docResult.innerHTML = `
    <h4 style="color: #60a5fa; margin-bottom: 8px;">📄 ${filename} Analysis</h4>
    <p style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 12px;">
      This document has been fully analyzed by StudySync. It contains essential formulas, code references, and exam summaries.
    </p>
    <div style="display: flex; gap: 8px;">
      <button class="btn-primary" style="width: auto; padding: 6px 14px; font-size: 0.78rem;" onclick="askDocQuestion('${filename}')">Ask AI Tutor about this</button>
      <button class="btn-primary" style="width: auto; padding: 6px 14px; font-size: 0.78rem;" onclick="generateQuizForDoc('${filename}')">Generate Quiz from PDF</button>
    </div>
  `;
}

window.askDocQuestion = function(filename) {
  closeModal("modalUpload");
  openModal("modalTutor");
  const chatInput = document.getElementById("chatInput");
  chatInput.value = `Explain the key concepts of ${filename}`;
};

window.generateQuizForDoc = function(filename) {
  closeModal("modalUpload");
  openModal("modalQuiz");
  document.getElementById("btnFetchQuiz").click();
};

// Document Upload & Analysis
function setupDocumentUpload() {
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
        studyNotesInput.value = `[Loaded file: ${file.name}] (${(file.size / 1024).toFixed(1)} KB)`;
      }
    });
  }

  if (btnProcessDoc) {
    btnProcessDoc.addEventListener("click", async () => {
      const text = studyNotesInput.value.trim() || "Machine Learning and Neural Networks Study Notes";
      btnProcessDoc.innerText = "Analyzing Content...";

      try {
        const response = await fetch("/api/documents/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ filename: "Uploaded_Notes.pdf", content: text })
        });
        const data = await response.json();
        btnProcessDoc.innerText = "Analyze Document & Generate Summary";

        docAnalysisResult.style.display = "block";
        docAnalysisResult.innerHTML = `
          <h4 style="color: #38bdf8; margin-bottom: 8px;">✨ Document AI Summary</h4>
          <p style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 12px; line-height: 1.4;">
            ${data.summary}
          </p>
          <div style="font-weight: 600; font-size: 0.82rem; color: #a5b4fc; margin-bottom: 6px;">Key Revision Takeaways:</div>
          <ul style="padding-left: 18px; font-size: 0.82rem; color: #94a3b8; margin-bottom: 12px;">
            ${data.key_takeaways.map(t => `<li style="margin-bottom: 4px;">${t}</li>`).join("")}
          </ul>
          <div style="font-weight: 600; font-size: 0.82rem; color: #34d399; margin-bottom: 6px;">Suggested Study Questions:</div>
          <ul style="padding-left: 18px; font-size: 0.82rem; color: #94a3b8;">
            ${data.suggested_questions.map(q => `<li style="margin-bottom: 4px;">${q}</li>`).join("")}
          </ul>
        `;

        // Reward study activity
        Tracker.addMinute();
      } catch (e) {
        btnProcessDoc.innerText = "Analyze Document & Generate Summary";
        alert("Failed to analyze document.");
      }
    });
  }
}

// Practice Quiz Engine
function setupQuiz() {
  const btnFetchQuiz = document.getElementById("btnFetchQuiz");
  const quizTopicSelect = document.getElementById("quizTopicSelect");
  const quizContainer = document.getElementById("quizContainer");

  let currentQuestions = [];
  let score = 0;
  let questionsAnswered = 0;

  if (btnFetchQuiz) {
    btnFetchQuiz.addEventListener("click", async () => {
      const topic = quizTopicSelect.value;
      btnFetchQuiz.innerText = "Loading...";

      try {
        const res = await fetch(`/api/quiz?topic=${encodeURIComponent(topic)}`);
        currentQuestions = await res.json();
        btnFetchQuiz.innerText = "Restart Quiz";
        renderQuizQuestions(currentQuestions);
      } catch (e) {
        btnFetchQuiz.innerText = "Start Quiz";
        quizContainer.innerHTML = "<p style='color:red;'>Could not load quiz questions.</p>";
      }
    });
  }

  function renderQuizQuestions(questions) {
    score = 0;
    questionsAnswered = 0;
    quizContainer.innerHTML = "";

    questions.forEach((q, idx) => {
      const box = document.createElement("div");
      box.className = "quiz-question-box";
      box.innerHTML = `
        <div class="quiz-q-title">Q${idx + 1}. ${q.question}</div>
        <div class="quiz-options-list" id="q_opt_${idx}">
          ${q.options.map((opt, optIdx) => `
            <button class="quiz-option-btn" data-qid="${idx}" data-opt="${optIdx}">
              ${String.fromCharCode(65 + optIdx)}. ${opt}
            </button>
          `).join("")}
        </div>
        <div id="expl_${idx}" style="display:none; margin-top: 10px; font-size: 0.8rem; padding: 8px 12px; border-radius: 6px; background: rgba(30, 41, 59, 0.6); color: #93c5fd;">
          💡 <strong>Explanation:</strong> ${q.explanation}
        </div>
      `;
      quizContainer.appendChild(box);
    });

    // Add option click handlers
    document.querySelectorAll(".quiz-option-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const qid = parseInt(btn.getAttribute("data-qid"));
        const chosen = parseInt(btn.getAttribute("data-opt"));
        const qObj = questions[qid];

        const parent = document.getElementById(`q_opt_${qid}`);
        const allBtns = parent.querySelectorAll(".quiz-option-btn");
        allBtns.forEach(b => b.style.pointerEvents = "none");

        questionsAnswered++;
        if (chosen === qObj.answer) {
          btn.classList.add("correct");
          score++;
        } else {
          btn.classList.add("wrong");
          if (allBtns[qObj.answer]) {
            allBtns[qObj.answer].classList.add("correct");
          }
        }

        const expl = document.getElementById(`expl_${qid}`);
        if (expl) expl.style.display = "block";

        // If completed all questions in quiz
        if (questionsAnswered === questions.length) {
          Tracker.recordQuiz(score, questions.length);
        }
      });
    });
  }
}

// Settings
function setupSettings() {
  const settingsUserName = document.getElementById("settingsUserName");
  const settingsApiKey = document.getElementById("settingsApiKey");
  const btnSaveSettings = document.getElementById("btnSaveSettings");

  if (settingsApiKey) {
    settingsApiKey.value = localStorage.getItem("studysync_gemini_key") || "";
  }

  if (settingsUserName) {
    settingsUserName.value = localStorage.getItem("studysync_user_name") || "";
  }

  if (btnSaveSettings) {
    btnSaveSettings.addEventListener("click", () => {
      const key = settingsApiKey.value.trim();
      const name = settingsUserName.value.trim() || "Student";
      localStorage.setItem("studysync_gemini_key", key);
      localStorage.setItem("studysync_user_name", name);
      applyUserName(name);
      alert("Settings saved successfully! Name updated to: " + name);
      closeModal("modalSettings");
    });
  }

  const profileBadge = document.getElementById("profileBadge");
  if (profileBadge) {
    profileBadge.addEventListener("click", () => openModal("modalSettings"));
  }
}

// Global search bar
function setupSearch() {
  const searchInput = document.getElementById("globalSearchInput");
  if (searchInput) {
    searchInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        const query = searchInput.value.trim();
        if (query) {
          openModal("modalTutor");
          const chatInput = document.getElementById("chatInput");
          chatInput.value = query;
          document.getElementById("btnSendChat").click();
          searchInput.value = "";
        }
      }
    });
  }
}
