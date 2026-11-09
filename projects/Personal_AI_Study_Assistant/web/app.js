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

  // Study Mode persona toggle button in header
  const btnStudyMode = document.getElementById("btnStudyModeToggle");
  const studyModeLabel = document.getElementById("studyModeLabel");
  const studyPersonas = [
    { id: "explainer", name: "Explainer 🎓", title: "Concept Explainer" },
    { id: "code", name: "Code Tutor 💻", title: "Code & Debug Tutor" },
    { id: "exam", name: "Exam Notes 📝", title: "Exam High-Yield Notes" },
    { id: "math", name: "Math Solver 🧮", title: "Step-by-Step Math Solver" }
  ];
  let currentPersonaIdx = 0;

  if (btnStudyMode) {
    btnStudyMode.addEventListener("click", () => {
      currentPersonaIdx = (currentPersonaIdx + 1) % studyPersonas.length;
      currentStudyMode = studyPersonas[currentPersonaIdx].id;
      if (studyModeLabel) {
        studyModeLabel.innerText = "Mode: " + studyPersonas[currentPersonaIdx].name;
      }
      showToast(`🎯 Active Study Persona: ${studyPersonas[currentPersonaIdx].title}`);
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

// GLOBAL STATE: Multi-turn conversation context & Active Study Persona
let currentStudyMode = "explainer";
let conversationHistory = [
  {
    role: "user",
    content: "Explain list comprehension in Python with an example."
  },
  {
    role: "assistant",
    content: "List comprehension is a concise way to create a new list from an existing iterable (like a list, tuple, etc.) using a single line of code. It makes your code shorter and easier to read."
  }
];

// CHAT & AI QUESTION ANSWERING (MULTI-TURN AWARE)
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

    // Save user turn in multi-turn conversation history
    conversationHistory.push({ role: "user", content: text });

    // Scroll to bottom
    chatStream.scrollTop = chatStream.scrollHeight;

    // Show assistant typing indicator
    const typingId = "typing_" + Date.now();
    appendTypingIndicator(typingId);
    chatStream.scrollTop = chatStream.scrollHeight;

    // Disable input and send button during AI generation
    if (sendBtn) {
      sendBtn.disabled = true;
      sendBtn.style.opacity = "0.5";
    }

    try {
      const apiKey = localStorage.getItem("studysync_gemini_key") || "";
      const model = localStorage.getItem("studysync_model") || "";

      // Send active question along with last 10 turns of conversation history and active mode
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: text,
          api_key: apiKey,
          model: model,
          mode: currentStudyMode,
          history: conversationHistory.slice(-10)
        })
      });

      const data = await response.json();
      removeTypingIndicator(typingId);

      const answer = data.answer || "I could not generate an answer at this moment.";
      const isRefusal = data.is_study_related === false || answer.includes("Sorry!");

      // ChatGPT-style character-by-character typewriter streaming!
      streamAssistantCard(answer, isRefusal, () => {
        if (!isRefusal) {
          // Record assistant answer into conversation history
          conversationHistory.push({ role: "assistant", content: answer });
          if (conversationHistory.length > 20) {
            conversationHistory = conversationHistory.slice(-20);
          }
          incrementStudyProgress();
        } else {
          // If query was non-study and refused, discard the user turn so history stays educational
          conversationHistory.pop();
        }
        if (sendBtn) {
          sendBtn.disabled = false;
          sendBtn.style.opacity = "1";
        }
        if (input) input.focus();
      });
    } catch (err) {
      conversationHistory.pop(); // discard failed attempt
      removeTypingIndicator(typingId);
      appendAssistantCard("⚠️ Network connection error. Please make sure the local server is running.", true);
      if (sendBtn) {
        sendBtn.disabled = false;
        sendBtn.style.opacity = "1";
      }
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

/**
 * ChatGPT-style character-by-character typewriter streaming
 */
function streamAssistantCard(rawMarkdown, isRefusal, onComplete) {
  const chatStream = document.getElementById("chatStream");
  const row = document.createElement("div");
  row.className = "message-row assistant-row";

  const cardDiv = document.createElement("div");
  cardDiv.className = `assistant-card ${isRefusal ? 'refusal-card' : ''}`;
  cardDiv.title = "Click to skip animation and show full answer instantly";

  const contentDiv = document.createElement("div");
  contentDiv.className = "card-streaming-content";

  const cursorSpan = document.createElement("span");
  cursorSpan.className = "chatgpt-cursor";

  const footerDiv = document.createElement("div");
  footerDiv.className = "card-footer";
  footerDiv.style.display = "none";

  const timeSpan = document.createElement("span");
  timeSpan.className = "footer-time";
  timeSpan.innerText = getCurrentTimeStr();

  const plainText = rawMarkdown.replace(/[`*#]/g, "");
  const copyBtn = document.createElement("button");
  copyBtn.className = "btn-copy-code";
  copyBtn.title = "Copy answer";
  copyBtn.setAttribute("data-copy", escapeHtml(plainText));
  copyBtn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="copy-svg"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>`;

  footerDiv.appendChild(timeSpan);
  footerDiv.appendChild(copyBtn);

  cardDiv.appendChild(contentDiv);
  cardDiv.appendChild(cursorSpan);
  cardDiv.appendChild(footerDiv);

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
  `;
  row.appendChild(cardDiv);
  chatStream.appendChild(row);

  // Click card to skip typing animation
  let isSkipped = false;
  cardDiv.addEventListener("click", (e) => {
    if (!e.target.closest(".btn-copy-code")) {
      isSkipped = true;
    }
  });

  // Typewriter streaming loop
  let charIndex = 0;
  const totalLength = rawMarkdown.length;
  // Natural pacing: 1 to 3 characters per frame depending on length
  const step = totalLength > 1200 ? 4 : (totalLength > 600 ? 2 : 1);
  const baseSpeed = totalLength > 1200 ? 8 : 14;

  function typeTick() {
    if (isSkipped) {
      charIndex = totalLength;
    } else {
      charIndex = Math.min(totalLength, charIndex + step);
    }

    const currentSlice = rawMarkdown.slice(0, charIndex);
    contentDiv.innerHTML = formatMarkdownResponse(currentSlice);

    // Keep scrolling smoothly to follow typing
    chatStream.scrollTop = chatStream.scrollHeight;

    if (charIndex < totalLength) {
      let delay = baseSpeed;
      const lastChar = rawMarkdown[charIndex - 1];
      if (lastChar === "." || lastChar === "?" || lastChar === "!") {
        delay = baseSpeed + 45; // natural pause at end of sentence
      } else if (lastChar === "\n") {
        delay = baseSpeed + 30; // pause at newline
      }
      setTimeout(typeTick, delay);
    } else {
      cursorSpan.remove();
      footerDiv.style.display = "flex";
      setupCopyButtons();
      chatStream.scrollTop = chatStream.scrollHeight;
      if (onComplete) onComplete();
    }
  }

  typeTick();
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
  if (!md) return "";

  let html = md;

  // Closed code blocks: ```lang ... ```
  html = html.replace(/```(?:python|py|javascript|js|html|css|sql|bash)?([\s\S]*?)```/g, (match, code) => {
    return `<div class="code-box"><code>${escapeHtml(code.trim())}</code></div>`;
  });

  // Handle open/unclosed code blocks while actively typewriter streaming
  html = html.replace(/```(?:python|py|javascript|js|html|css|sql|bash)?([\s\S]*)$/g, (match, code) => {
    return `<div class="code-box"><code>${escapeHtml(code.trim())}</code></div>`;
  });

  // Inline code: `code`
  html = html.replace(/`([^`\n]+)`/g, (match, code) => {
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

// QUICK ACTIONS (RIGHT SIDEBAR - CONTEXT-AWARE)
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
      const currentInput = input.value.trim();
      if (currentInput) {
        input.value = `Give a practical code or mathematical example for '${currentInput}' with line-by-line explanation.`;
      } else {
        input.value = "Give a practical coding or mathematical example with line-by-line explanation based on our discussion.";
      }
      sendBtn.click();
    });
  }

  if (qaSummarize) {
    qaSummarize.addEventListener("click", () => {
      const currentInput = input.value.trim();
      if (currentInput) {
        input.value = `Summarize '${currentInput}' into high-yield revision bullet points.`;
      } else {
        input.value = "Summarize the key study takeaways into concise revision bullet points.";
      }
      sendBtn.click();
    });
  }

  if (qaExplain) {
    qaExplain.addEventListener("click", () => {
      const currentInput = input.value.trim();
      if (currentInput) {
        input.value = `Explain '${currentInput}' in simple terms using an intuitive real-world analogy.`;
      } else {
        input.value = "Explain this concept in simple terms using an intuitive analogy.";
      }
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
  let uploadedFileName = "Urvashi_Study_Notes.pdf";

  if (btnSelectFile && fileUploadInput) {
    btnSelectFile.addEventListener("click", () => fileUploadInput.click());
    fileUploadInput.addEventListener("change", () => {
      if (fileUploadInput.files.length > 0) {
        const file = fileUploadInput.files[0];
        uploadedFileName = file.name;
        if (file.name.match(/\.(txt|md|py|js|html|css|json|csv)$/i)) {
          const reader = new FileReader();
          reader.onload = (e) => {
            studyNotesInput.value = e.target.result;
            showToast(`Loaded ${file.name}! Click 'Analyze Notes' below.`);
          };
          reader.readAsText(file);
        } else {
          studyNotesInput.value = `[Document selected: ${file.name} (${(file.size / 1024).toFixed(1)} KB)]\n\nStudy Notes and Chapter Concepts for ${file.name}.`;
        }
      }
    });
  }

  if (btnProcessDoc) {
    btnProcessDoc.addEventListener("click", async () => {
      const content = studyNotesInput.value.trim() || "Python OOP, Decorators and Algorithms Study Notes";
      btnProcessDoc.innerText = "Analyzing Notes with Groq AI...";
      btnProcessDoc.disabled = true;

      try {
        const apiKey = localStorage.getItem("studysync_gemini_key") || "";
        const model = localStorage.getItem("studysync_model") || "";
        const response = await fetch("/api/documents/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ filename: uploadedFileName, content: content, api_key: apiKey, model: model })
        });
        const data = await response.json();
        btnProcessDoc.innerText = "Analyze Notes with AI Assistant ⚡";
        btnProcessDoc.disabled = false;

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
        btnProcessDoc.disabled = false;
        showToast("Error processing notes. Please try again.");
      }
    });
  }
}

// PRACTICE QUIZ ENGINE (INTERACTIVE STEP-BY-STEP & ALL-QUESTIONS MODES)
function initQuizEngine() {
  const btnFetchQuiz = document.getElementById("btnFetchQuiz");
  const topicInput = document.getElementById("quizCustomTopic");
  const diffSelect = document.getElementById("quizDifficultySelect");
  const countSelect = document.getElementById("quizCountSelect");
  const container = document.getElementById("quizContainer");
  const progressStrip = document.getElementById("quizProgressStrip");
  const currentCounter = document.getElementById("quizCurrentCounter");
  const liveScore = document.getElementById("quizLiveScore");
  const progressFill = document.getElementById("quizProgressFill");
  const navPills = document.getElementById("quizNavPills");
  const scoreBanner = document.getElementById("quizScoreBanner");
  const scoreCircle = document.getElementById("quizScoreCircle");
  const scoreHeadline = document.getElementById("quizScoreHeadline");
  const scoreText = document.getElementById("quizScoreText");
  const scoreFeedback = document.getElementById("quizScoreFeedback");
  const btnRestart = document.getElementById("btnRestartQuiz");
  const btnNewQuiz = document.getElementById("btnNewQuiz");
  const btnModeStep = document.getElementById("btnQuizModeStep");
  const btnModeAll = document.getElementById("btnQuizModeAll");

  let questions = [];
  let userAnswers = {}; // { qIndex: selectedOptionIndex }
  let currentStep = 0;
  let quizMode = "step"; // "step" (one-by-one) or "all" (show all)

  // Mode switcher listeners
  if (btnModeStep && btnModeAll) {
    btnModeStep.addEventListener("click", () => {
      quizMode = "step";
      btnModeStep.classList.add("active");
      btnModeAll.classList.remove("active");
      if (questions.length > 0) renderQuiz();
    });

    btnModeAll.addEventListener("click", () => {
      quizMode = "all";
      btnModeAll.classList.add("active");
      btnModeStep.classList.remove("active");
      if (questions.length > 0) renderQuiz();
    });
  }

  // Fetch / Generate Quiz
  async function fetchQuiz() {
    const topic = topicInput.value.trim() || "Python Programming";
    const diff = diffSelect.value;
    const count = parseInt(countSelect.value, 10) || 10;
    const apiKey = localStorage.getItem("studysync_gemini_key") || "";
    const model = localStorage.getItem("studysync_model") || "";

    btnFetchQuiz.innerText = "Generating Quiz... ⚡";
    btnFetchQuiz.disabled = true;
    if (progressStrip) progressStrip.style.display = "none";
    if (scoreBanner) scoreBanner.style.display = "none";
    container.innerHTML = `
      <div style="text-align:center; padding:40px 20px;">
        <div style="font-size:2rem; margin-bottom:12px;">🧠⚡</div>
        <p style="font-size:0.95rem; font-weight:600; color:#38bdf8; margin-bottom:6px;">
          Crafting ${count} Fresh ${diff} Questions on '${escapeHtml(topic)}'...
        </p>
        <p style="font-size:0.82rem; color:#94a3b8;">
          Using Groq Cloud AI inference with diversity checking to avoid repeated questions.
        </p>
      </div>
    `;

    try {
      const url = `/api/quiz?topic=${encodeURIComponent(topic)}&difficulty=${encodeURIComponent(diff)}&count=${count}&api_key=${encodeURIComponent(apiKey)}&model=${encodeURIComponent(model)}&_t=${Date.now()}`;
      const res = await fetch(url);
      questions = await res.json();
      btnFetchQuiz.innerText = "Generate Quiz 🚀";
      btnFetchQuiz.disabled = false;

      if (!Array.isArray(questions) || questions.length === 0) {
        throw new Error("No questions returned.");
      }

      userAnswers = {};
      currentStep = 0;
      renderQuiz();
      showToast(`Generated ${questions.length} questions on ${topic}! 🎯`);
    } catch (err) {
      btnFetchQuiz.innerText = "Generate Quiz 🚀";
      btnFetchQuiz.disabled = false;
      container.innerHTML = `
        <div style="text-align:center; padding:30px; color:#f87171;">
          <p style="font-size:1rem; font-weight:700; margin-bottom:6px;">⚠️ Could not generate quiz questions.</p>
          <p style="font-size:0.84rem; color:#94a3b8; margin-bottom:14px;">Please check server connection or configure Groq API Key in Settings.</p>
          <button class="btn-glow-primary" id="btnRetryQuiz">Retry Now 🔄</button>
        </div>
      `;
      const retryBtn = document.getElementById("btnRetryQuiz");
      if (retryBtn) retryBtn.addEventListener("click", fetchQuiz);
    }
  }

  if (btnFetchQuiz) btnFetchQuiz.addEventListener("click", fetchQuiz);

  function getCalculatedScore() {
    let sc = 0;
    Object.keys(userAnswers).forEach((idxStr) => {
      const idx = parseInt(idxStr, 10);
      if (questions[idx] && userAnswers[idx] === questions[idx].answer) {
        sc++;
      }
    });
    return sc;
  }

  // Update progress bar and nav pills
  function updateProgressStrip() {
    if (!progressStrip) return;
    if (questions.length === 0) {
      progressStrip.style.display = "none";
      return;
    }

    progressStrip.style.display = "block";
    const answeredCount = Object.keys(userAnswers).length;
    const currentScore = getCalculatedScore();

    if (currentCounter) {
      currentCounter.innerText = `Question ${currentStep + 1} of ${questions.length}`;
    }
    if (liveScore) {
      liveScore.innerText = `Score: ${currentScore} / ${answeredCount}`;
    }
    if (progressFill) {
      const pct = Math.round(((currentStep + 1) / questions.length) * 100);
      progressFill.style.width = `${pct}%`;
    }

    if (navPills) {
      navPills.innerHTML = questions.map((_, idx) => {
        let stateClass = "";
        if (idx === currentStep && quizMode === "step") {
          stateClass = "active";
        } else if (idx in userAnswers) {
          stateClass = (userAnswers[idx] === questions[idx].answer) ? "correct" : "wrong";
        }
        return `
          <button class="quiz-nav-pill ${stateClass}" data-step="${idx}" title="Jump to Q${idx + 1}">
            ${idx + 1}
          </button>
        `;
      }).join("");

      navPills.querySelectorAll(".quiz-nav-pill").forEach((pill) => {
        pill.addEventListener("click", () => {
          const step = parseInt(pill.getAttribute("data-step"), 10);
          currentStep = step;
          if (quizMode === "step") {
            renderStepCard();
          } else {
            const el = document.getElementById(`quiz_q_box_${step}`);
            if (el) el.scrollIntoView({ behavior: "smooth", block: "center" });
          }
          updateProgressStrip();
        });
      });
    }
  }

  // Render the quiz based on active mode
  function renderQuiz() {
    if (scoreBanner) scoreBanner.style.display = "none";
    updateProgressStrip();

    if (quizMode === "step") {
      renderStepCard();
    } else {
      renderAllQuestions();
    }
  }

  // Helper to format code blocks inside question text
  function formatQuestionText(text) {
    if (!text) return "";
    let formatted = escapeHtml(text);
    // Render code blocks ```python ... ```
    formatted = formatted.replace(/```(?:python|py|javascript|js|sql)?([\s\S]*?)```/g, (match, code) => {
      return `<div class="code-box" style="margin:8px 0; background:#050811;"><code>${code.trim()}</code></div>`;
    });
    // Render inline code `...`
    formatted = formatted.replace(/`([^`]+)`/g, '<code style="background:#090e1c; color:#38bdf8; padding:2px 6px; border-radius:4px; font-family:\'JetBrains Mono\',monospace;">$1</code>');
    formatted = formatted.replace(/\n/g, '<br>');
    return formatted;
  }

  // STEP-BY-STEP (ONE-BY-ONE) RENDER
  function renderStepCard() {
    const q = questions[currentStep];
    if (!q) return;

    const isAnswered = currentStep in userAnswers;
    const selectedOid = isAnswered ? userAnswers[currentStep] : null;
    const isLast = currentStep === questions.length - 1;

    container.innerHTML = `
      <div class="quiz-step-card">
        <div class="quiz-step-header">
          <span style="font-weight:700; color:#38bdf8; font-size:0.92rem;">
            Question ${currentStep + 1} of ${questions.length}
          </span>
          <span class="quiz-difficulty-tag">${escapeHtml(diffSelect.value || "Intermediate")}</span>
        </div>

        <div class="quiz-q-title" style="font-size:1.02rem; line-height:1.5; margin-bottom:16px;">
          ${formatQuestionText(q.question)}
        </div>

        <div class="quiz-options-grid" id="step_options_grid">
          ${q.options.map((opt, oIdx) => {
            let optClass = "quiz-opt-btn";
            if (isAnswered) {
              if (oIdx === q.answer) {
                optClass += " correct";
              } else if (oIdx === selectedOid) {
                optClass += " wrong";
              }
            }
            return `
              <button class="${optClass}" data-oid="${oIdx}" style="${isAnswered ? 'pointer-events:none;' : ''}">
                <strong style="margin-right:8px; color:#a5b4fc;">${String.fromCharCode(65 + oIdx)}.</strong> ${escapeHtml(opt)}
              </button>
            `;
          }).join("")}
        </div>

        <div id="step_explanation_box" style="display:${isAnswered ? 'block' : 'none'}; margin-top:14px; font-size:0.85rem; padding:12px 14px; border-radius:8px; background:rgba(30,41,59,0.7); border:1px solid rgba(99,102,241,0.3); color:#93c5fd; line-height:1.45;">
          💡 <strong>Explanation:</strong> ${escapeHtml(q.explanation)}
        </div>

        <div class="quiz-step-nav-row">
          <button class="btn-outline-subtle" id="btnStepPrev" ${currentStep === 0 ? "disabled style='opacity:0.4; cursor:not-allowed;'" : ""}>
            ⬅ Previous
          </button>

          <div style="display:flex; gap:8px;">
            ${!isLast ? `
              <button class="btn-glow-primary" id="btnStepNext">
                Next Question ➔
              </button>
            ` : `
              <button class="btn-glow-primary" id="btnStepFinish" style="background:linear-gradient(135deg, #10b981, #059669);">
                Finish & View Results 🏆
              </button>
            `}
          </div>
        </div>
      </div>
    `;

    // Option click handling
    const optButtons = container.querySelectorAll("#step_options_grid .quiz-opt-btn");
    optButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        if (currentStep in userAnswers) return;
        const oid = parseInt(btn.getAttribute("data-oid"), 10);
        userAnswers[currentStep] = oid;

        optButtons.forEach(b => b.style.pointerEvents = "none");

        if (oid === q.answer) {
          btn.classList.add("correct");
        } else {
          btn.classList.add("wrong");
          if (optButtons[q.answer]) optButtons[q.answer].classList.add("correct");
        }

        const expl = document.getElementById("step_explanation_box");
        if (expl) expl.style.display = "block";

        updateProgressStrip();

        // If all questions are answered, check completion
        if (Object.keys(userAnswers).length === questions.length) {
          incrementStudyProgress();
        }
      });
    });

    // Navigation buttons
    const prevBtn = document.getElementById("btnStepPrev");
    if (prevBtn && currentStep > 0) {
      prevBtn.addEventListener("click", () => {
        currentStep--;
        renderStepCard();
        updateProgressStrip();
      });
    }

    const nextBtn = document.getElementById("btnStepNext");
    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        if (currentStep < questions.length - 1) {
          currentStep++;
          renderStepCard();
          updateProgressStrip();
        }
      });
    }

    const finishBtn = document.getElementById("btnStepFinish");
    if (finishBtn) {
      finishBtn.addEventListener("click", () => {
        showResultsSummary();
      });
    }
  }

  // ALL QUESTIONS RENDER MODE
  function renderAllQuestions() {
    container.innerHTML = "";

    questions.forEach((q, idx) => {
      const box = document.createElement("div");
      box.className = "quiz-q-box";
      box.id = `quiz_q_box_${idx}`;

      const isAnswered = idx in userAnswers;
      const selectedOid = isAnswered ? userAnswers[idx] : null;

      box.innerHTML = `
        <div class="quiz-q-title">Q${idx + 1}. ${formatQuestionText(q.question)}</div>
        <div class="quiz-options-grid" id="q_opts_${idx}">
          ${q.options.map((opt, oIdx) => {
            let optClass = "quiz-opt-btn";
            if (isAnswered) {
              if (oIdx === q.answer) optClass += " correct";
              else if (oIdx === selectedOid) optClass += " wrong";
            }
            return `
              <button class="${optClass}" data-qid="${idx}" data-oid="${oIdx}" style="${isAnswered ? 'pointer-events:none;' : ''}">
                <strong style="margin-right:8px; color:#a5b4fc;">${String.fromCharCode(65 + oIdx)}.</strong> ${escapeHtml(opt)}
              </button>
            `;
          }).join("")}
        </div>
        <div id="q_expl_${idx}" style="display:${isAnswered ? 'block' : 'none'}; margin-top:10px; font-size:0.82rem; padding:8px 12px; border-radius:6px; background:rgba(30,41,59,0.7); color:#93c5fd;">
          💡 <strong>Explanation:</strong> ${escapeHtml(q.explanation)}
        </div>
      `;
      container.appendChild(box);
    });

    container.querySelectorAll(".quiz-opt-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const qid = parseInt(btn.getAttribute("data-qid"), 10);
        const oid = parseInt(btn.getAttribute("data-oid"), 10);
        if (qid in userAnswers) return;

        userAnswers[qid] = oid;
        const qObj = questions[qid];
        const parent = document.getElementById(`q_opts_${qid}`);
        const allBtns = parent.querySelectorAll(".quiz-opt-btn");
        allBtns.forEach(b => b.style.pointerEvents = "none");

        if (oid === qObj.answer) {
          btn.classList.add("correct");
        } else {
          btn.classList.add("wrong");
          if (allBtns[qObj.answer]) allBtns[qObj.answer].classList.add("correct");
        }

        const expl = document.getElementById(`q_expl_${qid}`);
        if (expl) expl.style.display = "block";

        updateProgressStrip();

        if (Object.keys(userAnswers).length === questions.length) {
          showResultsSummary();
          incrementStudyProgress();
        }
      });
    });
  }

  // SHOW RESULTS SUMMARY SCREEN
  function showResultsSummary() {
    if (progressStrip) progressStrip.style.display = "none";
    if (!scoreBanner) return;

    const total = questions.length;
    const finalScore = getCalculatedScore();
    const pct = total > 0 ? Math.round((finalScore / total) * 100) : 0;

    scoreBanner.style.display = "flex";
    if (scoreCircle) {
      scoreCircle.innerText = `${pct}%`;
      if (pct >= 80) {
        scoreCircle.style.background = "linear-gradient(135deg, #10b981, #059669)";
      } else if (pct >= 50) {
        scoreCircle.style.background = "linear-gradient(135deg, #6366f1, #a855f7)";
      } else {
        scoreCircle.style.background = "linear-gradient(135deg, #f59e0b, #d97706)";
      }
    }

    if (scoreHeadline) {
      if (pct === 100) scoreHeadline.innerText = "🏆 Flawless Victory! Perfect Score!";
      else if (pct >= 80) scoreHeadline.innerText = "🎉 Outstanding Performance!";
      else if (pct >= 50) scoreHeadline.innerText = "👍 Solid Effort! Good Knowledge!";
      else scoreHeadline.innerText = "📚 Keep Practicing & Review Concepts!";
    }

    if (scoreText) {
      scoreText.innerText = `Score: ${finalScore} / ${total} (${pct}%)`;
    }

    if (scoreFeedback) {
      const unanswered = total - Object.keys(userAnswers).length;
      if (unanswered > 0) {
        scoreFeedback.innerText = `You completed ${Object.keys(userAnswers).length} of ${total} questions. Review your answers below:`;
      } else if (pct >= 80) {
        scoreFeedback.innerText = "You have demonstrated strong conceptual command over this study topic!";
      } else {
        scoreFeedback.innerText = "Review the explanations below to reinforce key academic principles.";
      }
    }

    // Render detailed review summary
    let reviewHtml = `
      <div class="quiz-review-wrap">
        <h4 style="color:#a5b4fc; font-size:0.95rem; margin-bottom:12px; display:flex; align-items:center; gap:6px;">
          <span>📋</span> Question by Question Review
        </h4>
    `;

    questions.forEach((q, idx) => {
      const isAns = idx in userAnswers;
      const userChoice = isAns ? userAnswers[idx] : null;
      const isCorrect = isAns && (userChoice === q.answer);

      let statusBadge = `<span style="color:#f87171; font-weight:700;">❌ Incorrect</span>`;
      if (isCorrect) statusBadge = `<span style="color:#34d399; font-weight:700;">✅ Correct</span>`;
      else if (!isAns) statusBadge = `<span style="color:#94a3b8; font-weight:700;">⚪ Unanswered</span>`;

      reviewHtml += `
        <div class="quiz-review-item">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
            <strong style="color:#ffffff; font-size:0.9rem;">Q${idx + 1}. ${escapeHtml(q.question)}</strong>
            <span style="font-size:0.78rem; margin-left:12px; white-space:nowrap;">${statusBadge}</span>
          </div>

          <div style="font-size:0.83rem; color:#cbd5e1; margin-bottom:4px;">
            ${isAns ? `Your Answer: <strong style="color:${isCorrect ? '#34d399' : '#f87171'}">${String.fromCharCode(65 + userChoice)}. ${escapeHtml(q.options[userChoice])}</strong>` : '<em style="color:#94a3b8;">Not attempted</em>'}
          </div>

          ${!isCorrect ? `
            <div style="font-size:0.83rem; color:#34d399; margin-bottom:6px;">
              Correct Answer: <strong>${String.fromCharCode(65 + q.answer)}. ${escapeHtml(q.options[q.answer])}</strong>
            </div>
          ` : ''}

          <div style="font-size:0.8rem; color:#93c5fd; background:rgba(30,41,59,0.5); padding:6px 10px; border-radius:6px; margin-top:6px;">
            💡 ${escapeHtml(q.explanation)}
          </div>
        </div>
      `;
    });

    reviewHtml += "</div>";
    container.innerHTML = reviewHtml;
  }

  // Retake same quiz questions
  if (btnRestart) {
    btnRestart.addEventListener("click", () => {
      userAnswers = {};
      currentStep = 0;
      renderQuiz();
      showToast("Quiz reset! Try to score 100%! 🚀");
    });
  }

  // Generate a brand new fresh set of questions
  if (btnNewQuiz) {
    btnNewQuiz.addEventListener("click", () => {
      fetchQuiz();
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
      btnGenCards.disabled = true;

      try {
        const apiKey = localStorage.getItem("studysync_gemini_key") || "";
        const model = localStorage.getItem("studysync_model") || "";
        const res = await fetch("/api/flashcards", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ topic: topic, count: 5, api_key: apiKey, model: model })
        });
        const data = await res.json();
        btnGenCards.innerText = "Generate Cards 📇";
        btnGenCards.disabled = false;

        if (data.flashcards && data.flashcards.length > 0) {
          cards = data.flashcards.map(c => ({ q: c.front, a: c.back }));
          currentIndex = 0;
          updateCard();
          showToast(`Generated 5 cards on ${topic}!`);
        }
      } catch (err) {
        btnGenCards.innerText = "Generate Cards 📇";
        btnGenCards.disabled = false;
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
        if (data.success || data.status === "connected") {
          statusMsg.style.color = "#34d399";
          statusMsg.innerText = "✅ Groq Cloud connection verified! " + (data.message || "Ultra-fast response active.");
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
