/**
 * Expense Tracker - Frontend App Logic
 * Connects with Python local REST API and provides interactive UI.
 */

let allTransactions = [];
let analyticsData = {};
let currentChartMode = 'monthly'; // 'monthly' or 'cumulative'
let hoveredMonthIndex = null;
let chartXPositions = [];
let currentIncValues = [];
let currentExpValues = [];

const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

document.addEventListener('DOMContentLoaded', () => {
  initDateBadge();
  setupNavButtons();
  setupChartControls();
  setupModals();
  setupForm();
  setupWindowControls();
  loadData();
});

// Format Indian Rupee currency
function formatINR(val) {
  const num = parseFloat(val) || 0;
  return '₹ ' + num.toLocaleString('en-IN', { maximumFractionDigits: 2 });
}

// 1. Dynamic Date Display in Header
function initDateBadge() {
  const now = new Date();
  const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
  const dateStr = now.toLocaleDateString('en-GB', options);
  const dateText = document.getElementById('dateText');
  if (dateText) {
    dateText.innerText = dateStr;
  }
  const inputDate = document.getElementById('inputDate');
  if (inputDate) {
    inputDate.value = now.toISOString().split('T')[0];
  }
}

// 2. Fetch Data from Backend API
async function loadData() {
  try {
    const [txRes, anRes] = await Promise.all([
      fetch('/api/transactions'),
      fetch('/api/analytics')
    ]);

    allTransactions = await txRes.json();
    analyticsData = await anRes.json();

    renderSummaryCards();
    renderRecentTransactions();
    renderOverviewChart();
  } catch (err) {
    console.error('Failed to load data:', err);
    // Offline / fallback calculation if API hasn't loaded yet
    renderOverviewChart();
  }
}

// 3. Render 3 Summary Cards
function renderSummaryCards() {
  const incEl = document.getElementById('totalIncomeVal');
  const expEl = document.getElementById('totalExpenseVal');
  const balEl = document.getElementById('totalBalanceVal');

  const inc = analyticsData.total_income || 0;
  const exp = analyticsData.total_expense || 0;
  const bal = analyticsData.balance || 0;

  if (incEl) incEl.innerText = formatINR(inc);
  if (expEl) expEl.innerText = formatINR(exp);
  if (balEl) balEl.innerText = formatINR(bal);
}

// 4. Render Recent Transactions Table / Empty State
function renderRecentTransactions() {
  const tbody = document.getElementById('recentTransactionsBody');
  const emptyWrap = document.getElementById('emptyStateWrap');
  if (!tbody || !emptyWrap) return;

  tbody.innerHTML = '';

  if (!allTransactions || allTransactions.length === 0) {
    emptyWrap.style.display = 'flex';
    return;
  }

  emptyWrap.style.display = 'none';

  // Sort descending by date or id, show top 5
  const recents = [...allTransactions].reverse().slice(0, 5);

  recents.forEach(tx => {
    const tr = document.createElement('tr');
    const isInc = (tx.type || 'Expense').toLowerCase() === 'income';

    const catEmoji = getCategoryEmoji(tx.user_catagery);
    const amtSign = isInc ? '+' : '-';
    const amtClass = isInc ? 'amount-income' : 'amount-expense';
    const typeBadgeClass = isInc ? 'income' : 'expense';

    tr.innerHTML = `
      <td>${escapeHtml(tx.user_date || 'Today')}</td>
      <td>
        <strong>${escapeHtml(tx.user_title || 'Untitled')}</strong>
        <span class="category-pill">${catEmoji} ${escapeHtml(tx.user_catagery || 'General')}</span>
      </td>
      <td>
        <span class="type-badge ${typeBadgeClass}">${isInc ? 'Income' : 'Expense'}</span>
      </td>
      <td style="text-align: right;">
        <span class="${amtClass}">${amtSign}${formatINR(tx.user_amount)}</span>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function getCategoryEmoji(cat) {
  const map = {
    food: '🍔',
    travel: '🚗',
    shopping: '🛍️',
    bills: '💡',
    entertainment: '🎬',
    health: '🏥',
    education: '📚',
    salary: '💼',
    investment: '📈',
    other: '🏷️'
  };
  const key = (cat || '').toLowerCase().trim();
  return map[key] || '💳';
}

function escapeHtml(str) {
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Dynamic Y-Axis Scale Calculator based on data magnitude
function getNiceYScale(maxVal) {
  if (maxVal <= 0) {
    return { max: 1500, steps: [0, 500, 1000, 1500] };
  }

  const rawStep = maxVal / 3.2;
  const power = Math.pow(10, Math.floor(Math.log10(rawStep)));
  const frac = rawStep / power;

  let step;
  if (frac <= 1.2) step = 1 * power;
  else if (frac <= 2.2) step = 2 * power;
  else if (frac <= 3.2) step = 2.5 * power;
  else if (frac <= 7.0) step = 5 * power;
  else step = 10 * power;

  const steps = [0];
  let curr = step;
  while (steps[steps.length - 1] < maxVal || steps.length < 4) {
    steps.push(curr);
    curr += step;
  }
  return { max: steps[steps.length - 1], steps: steps };
}

function formatYTick(val) {
  if (val === 0) return '0';
  if (val >= 10000 && val % 1000 === 0) {
    return (val / 1000) + 'k';
  }
  return val.toLocaleString('en-IN');
}

// 5. Draw Dynamic, Accurate Chart on Canvas
function renderOverviewChart() {
  const canvas = document.getElementById('overviewChartCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  // Handle Retina / HiDPI crispness
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.parentElement.getBoundingClientRect();
  const width = rect.width > 200 ? rect.width : 620;
  const height = 210;

  canvas.width = width * dpr;
  canvas.height = height * dpr;
  canvas.style.width = width + 'px';
  canvas.style.height = height + 'px';

  ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, width, height);

  const padLeft = 52;
  const padRight = 24;
  const padTop = 22;
  const padBottom = 26;

  const chartW = width - padLeft - padRight;
  const chartH = height - padTop - padBottom;
  const baselineY = padTop + chartH;

  // Extract base series data from analyticsData
  const rawInc = analyticsData.monthly_income || [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  const rawExp = analyticsData.monthly_expense || [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

  // Process data based on Current View Mode (Monthly vs Cumulative)
  if (currentChartMode === 'cumulative') {
    currentIncValues = [];
    currentExpValues = [];
    let sumInc = 0;
    let sumExp = 0;
    for (let i = 0; i < 12; i++) {
      sumInc += (rawInc[i] || 0);
      sumExp += (rawExp[i] || 0);
      currentIncValues.push(sumInc);
      currentExpValues.push(sumExp);
    }
  } else {
    currentIncValues = [...rawInc];
    currentExpValues = [...rawExp];
  }

  // Calculate Dynamic Y-Scale so high values (e.g., 5000) fit with comfortable headroom
  const maxDataVal = Math.max(0, ...currentIncValues, ...currentExpValues);
  const scale = getNiceYScale(maxDataVal);
  const maxVal = scale.max;
  const ySteps = scale.steps;

  // Draw Horizontal Gridlines & Y-Axis Labels
  ctx.font = '600 11px Nunito, sans-serif';
  ctx.textAlign = 'right';
  ctx.textBaseline = 'middle';

  ySteps.forEach(step => {
    const y = padTop + chartH - (step / maxVal) * chartH;
    
    // Label
    ctx.fillStyle = '#64748b';
    ctx.fillText(formatYTick(step), padLeft - 10, y);

    // Gridline
    ctx.beginPath();
    ctx.strokeStyle = (step === 0) ? '#334155' : '#e2e8f0';
    ctx.lineWidth = (step === 0) ? 1.4 : 1;
    ctx.moveTo(padLeft, y);
    ctx.lineTo(width - padRight, y);
    ctx.stroke();
  });

  // Calculate X-Positions for all 12 Months
  chartXPositions = [];
  ctx.textAlign = 'center';
  ctx.textBaseline = 'top';

  MONTHS.forEach((m, idx) => {
    const x = padLeft + (idx / (MONTHS.length - 1)) * chartW;
    chartXPositions.push(x);

    const isHovered = hoveredMonthIndex === idx;
    ctx.font = isHovered ? 'bold 11.5px Nunito, sans-serif' : '600 11px Nunito, sans-serif';
    ctx.fillStyle = isHovered ? '#6d28d9' : '#64748b';
    ctx.fillText(m, x, baselineY + 8);
  });

  // Draw Vertical Guide Line if a Month is Hovered
  if (hoveredMonthIndex !== null && chartXPositions[hoveredMonthIndex]) {
    const hx = chartXPositions[hoveredMonthIndex];
    ctx.save();
    ctx.beginPath();
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = '#a78bfa';
    ctx.lineWidth = 1.5;
    ctx.moveTo(hx, padTop);
    ctx.lineTo(hx, baselineY);
    ctx.stroke();
    ctx.restore();
  }

  const hasData = currentIncValues.some(v => v > 0) || currentExpValues.some(v => v > 0);

  if (hasData) {
    // 1. Draw Income Spline (Green)
    const incPoints = chartXPositions.map((x, i) => {
      const val = currentIncValues[i] || 0;
      const y = baselineY - (val / maxVal) * chartH;
      return { x, y, val };
    });
    drawSmoothSpline(ctx, incPoints, baselineY, '#10b981', 'rgba(16, 185, 129, 0.12)', 'income');

    // 2. Draw Expense Spline (Purple)
    const expPoints = chartXPositions.map((x, i) => {
      const val = currentExpValues[i] || 0;
      const y = baselineY - (val / maxVal) * chartH;
      return { x, y, val };
    });
    drawSmoothSpline(ctx, expPoints, baselineY, '#7c43ea', 'rgba(124, 67, 234, 0.15)', 'expense');
  }
}

// Catmull-Rom Cubic Spline that GUARANTEES points lie 100% on the line!
function drawSmoothSpline(ctx, points, baselineY, strokeColor, fillColor, seriesType) {
  if (!points || points.length === 0) return;

  ctx.save();
  ctx.beginPath();
  ctx.moveTo(points[0].x, points[0].y);

  const tension = 0.28;

  for (let i = 0; i < points.length - 1; i++) {
    const p0 = i > 0 ? points[i - 1] : points[i];
    const p1 = points[i];
    const p2 = points[i + 1];
    const p3 = i < points.length - 2 ? points[i + 2] : p2;

    // Keep flat along baseline if both consecutive values are 0
    if (p1.val === 0 && p2.val === 0) {
      ctx.lineTo(p2.x, baselineY);
      continue;
    }

    const cp1x = p1.x + (p2.x - p0.x) * tension;
    let cp1y = p1.y + (p2.y - p0.y) * tension;

    const cp2x = p2.x - (p3.x - p1.x) * tension;
    let cp2y = p2.y - (p3.y - p1.y) * tension;

    // Never dip below baseline
    if (cp1y > baselineY) cp1y = baselineY;
    if (cp2y > baselineY) cp2y = baselineY;

    ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, p2.x, p2.y);
  }

  // Draw the smooth curve
  ctx.strokeStyle = strokeColor;
  ctx.lineWidth = 2.8;
  ctx.lineJoin = 'round';
  ctx.lineCap = 'round';
  ctx.stroke();

  // Area Fill under curve
  ctx.lineTo(points[points.length - 1].x, baselineY);
  ctx.lineTo(points[0].x, baselineY);
  ctx.closePath();
  ctx.fillStyle = fillColor;
  ctx.fill();

  // Draw Centered Point Dots & Value Badges on the Curve
  points.forEach((p, idx) => {
    if (p.val > 0) {
      const isHovered = hoveredMonthIndex === idx;

      // Outer glow circle
      ctx.beginPath();
      ctx.arc(p.x, p.y, isHovered ? 7 : 5, 0, Math.PI * 2);
      ctx.fillStyle = strokeColor;
      ctx.fill();

      // Inner crisp white center
      ctx.beginPath();
      ctx.arc(p.x, p.y, isHovered ? 3.5 : 2.5, 0, Math.PI * 2);
      ctx.fillStyle = '#ffffff';
      ctx.fill();

      // Value Pill Badge above point
      // Offset if income & expense are close
      let badgeY = p.y - 10;
      if (seriesType === 'income' && currentExpValues[idx] > 0 && Math.abs(currentIncValues[idx] - currentExpValues[idx]) < 500) {
        badgeY = p.y - 18;
      }
      drawValueBadge(ctx, p.x, badgeY, p.val, strokeColor, isHovered);
    }
  });

  ctx.restore();
}

function drawValueBadge(ctx, x, y, val, color, isHovered) {
  const text = '₹' + Math.round(val).toLocaleString('en-IN');
  ctx.font = isHovered ? 'bold 11px Nunito, sans-serif' : '700 9.5px Nunito, sans-serif';
  const textW = ctx.measureText(text).width;
  const padX = 6;
  const padY = 2;
  const bW = textW + padX * 2;
  const bH = 16;
  const bX = Math.max(10, Math.min(x - bW / 2, (ctx.canvas.width / (window.devicePixelRatio || 1)) - bW - 10));
  const bY = y - bH;

  ctx.save();
  ctx.beginPath();
  const r = 4;
  ctx.moveTo(bX + r, bY);
  ctx.lineTo(bX + bW - r, bY);
  ctx.quadraticCurveTo(bX + bW, bY, bX + bW, bY + r);
  ctx.lineTo(bX + bW, bY + bH - r);
  ctx.quadraticCurveTo(bX + bW, bY + bH, bX + bW - r, bY + bH);
  ctx.lineTo(bX + r, bY + bH);
  ctx.quadraticCurveTo(bX, bY + bH, bX, bY + bH - r);
  ctx.lineTo(bX, bY + r);
  ctx.quadraticCurveTo(bX, bY, bX + r, bY);
  ctx.closePath();

  ctx.fillStyle = color;
  ctx.fill();

  ctx.fillStyle = '#ffffff';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(text, bX + bW / 2, bY + bH / 2 + 0.5);
  ctx.restore();
}

// Setup Chart View Toggle and Hover Listeners
function setupChartControls() {
  const btnMonthly = document.getElementById('btnChartMonthly');
  const btnCumulative = document.getElementById('btnChartCumulative');

  if (btnMonthly && btnCumulative) {
    btnMonthly.addEventListener('click', () => {
      currentChartMode = 'monthly';
      btnMonthly.classList.add('active');
      btnCumulative.classList.remove('active');
      renderOverviewChart();
    });

    btnCumulative.addEventListener('click', () => {
      currentChartMode = 'cumulative';
      btnCumulative.classList.add('active');
      btnMonthly.classList.remove('active');
      renderOverviewChart();
    });
  }

  const canvas = document.getElementById('overviewChartCanvas');
  const tooltip = document.getElementById('chartTooltip');

  if (canvas) {
    canvas.addEventListener('mousemove', (e) => {
      const rect = canvas.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;

      if (!chartXPositions || chartXPositions.length === 0) return;

      let closestIdx = 0;
      let minDist = Infinity;
      chartXPositions.forEach((x, idx) => {
        const dist = Math.abs(mouseX - x);
        if (dist < minDist) {
          minDist = dist;
          closestIdx = idx;
        }
      });

      if (minDist < 35) {
        hoveredMonthIndex = closestIdx;
        renderOverviewChart();

        if (tooltip) {
          const inc = currentIncValues[closestIdx] || 0;
          const exp = currentExpValues[closestIdx] || 0;
          tooltip.style.display = 'block';
          tooltip.style.left = chartXPositions[closestIdx] + 'px';
          tooltip.style.top = '36px';
          tooltip.innerHTML = `
            <div style="font-size:0.85rem; font-weight:800; margin-bottom:2px;">${MONTHS[closestIdx]} 2026</div>
            <div style="color:#10b981;">● Income: ${formatINR(inc)}</div>
            <div style="color:#c084fc;">● Expense: ${formatINR(exp)}</div>
          `;
        }
      } else {
        hoveredMonthIndex = null;
        if (tooltip) tooltip.style.display = 'none';
        renderOverviewChart();
      }
    });

    canvas.addEventListener('mouseleave', () => {
      hoveredMonthIndex = null;
      if (tooltip) tooltip.style.display = 'none';
      renderOverviewChart();
    });
  }
}

// 6. Navigation Buttons Listener
function setupNavButtons() {
  const navAdd = document.getElementById('btnNavAdd');
  const navView = document.getElementById('btnNavView');
  const navSearch = document.getElementById('btnNavSearch');
  const navDelete = document.getElementById('btnNavDelete');
  const navTotal = document.getElementById('btnNavTotal');
  const navExit = document.getElementById('btnNavExit');
  const btnEmptyAdd = document.getElementById('btnEmptyAdd');
  const btnViewAll = document.getElementById('btnViewAll');

  if (navAdd) navAdd.addEventListener('click', () => openAddModal());
  if (btnEmptyAdd) btnEmptyAdd.addEventListener('click', () => openAddModal());
  if (navView) navView.addEventListener('click', () => openViewAllModal());
  if (btnViewAll) btnViewAll.addEventListener('click', () => openViewAllModal());
  if (navSearch) navSearch.addEventListener('click', () => openSearchModal());
  if (navDelete) navDelete.addEventListener('click', () => openDeleteModal());
  if (navTotal) navTotal.addEventListener('click', () => openTotalModal());
  if (navExit) navExit.addEventListener('click', () => handleExit());
}

// 7. Modals Management
function setupModals() {
  // Close on backdrop or close button
  document.querySelectorAll('[data-close]').forEach(btn => {
    btn.addEventListener('click', () => {
      const modalId = btn.getAttribute('data-close');
      closeModal(modalId);
    });
  });

  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('open');
      }
    });
  });

  // Type Toggle inside Form
  const btnExp = document.getElementById('btnTypeExpense');
  const btnInc = document.getElementById('btnTypeIncome');
  if (btnExp && btnInc) {
    btnExp.addEventListener('click', () => {
      btnExp.classList.add('active');
      btnInc.classList.remove('active');
    });
    btnInc.addEventListener('click', () => {
      btnInc.classList.add('active');
      btnExp.classList.remove('active');
    });
  }

  // Live Search listener
  const liveInput = document.getElementById('liveSearchInput');
  if (liveInput) {
    liveInput.addEventListener('input', (e) => handleLiveSearch(e.target.value));
  }

  // Delete Action Confirm
  const btnConfirmDel = document.getElementById('btnConfirmDelete');
  if (btnConfirmDel) {
    btnConfirmDel.addEventListener('click', handleConfirmDelete);
  }

  // Export CSV
  const btnExport = document.getElementById('btnExportCsv');
  if (btnExport) {
    btnExport.addEventListener('click', handleExportCsv);
  }

  // View Filter Listeners
  const viewFilterCat = document.getElementById('viewFilterCategory');
  const viewFilterType = document.getElementById('viewFilterType');
  const viewSearchInput = document.getElementById('viewSearchInput');
  [viewFilterCat, viewFilterType, viewSearchInput].forEach(el => {
    if (el) el.addEventListener('input', renderViewAllTable);
  });
}

function openModal(id) {
  const m = document.getElementById(id);
  if (m) m.classList.add('open');
}

function closeModal(id) {
  const m = document.getElementById(id);
  if (m) m.classList.remove('open');
}

function openAddModal(editTx = null) {
  const form = document.getElementById('expenseForm');
  const titleEl = document.getElementById('modalFormTitle');
  const idEl = document.getElementById('editExpenseId');
  const btnExp = document.getElementById('btnTypeExpense');
  const btnInc = document.getElementById('btnTypeIncome');

  form.reset();
  initDateBadge();

  if (editTx) {
    titleEl.innerText = '✏️ Edit Transaction';
    idEl.value = editTx.user_id;
    document.getElementById('inputTitle').value = editTx.user_title;
    document.getElementById('inputAmount').value = editTx.user_amount;
    document.getElementById('inputCategory').value = editTx.user_catagery || 'Food';
    document.getElementById('inputDate').value = editTx.user_date || '';

    if ((editTx.type || 'Expense').toLowerCase() === 'income') {
      btnInc.classList.add('active');
      btnExp.classList.remove('active');
    } else {
      btnExp.classList.add('active');
      btnInc.classList.remove('active');
    }
  } else {
    titleEl.innerText = '✨ Add Transaction';
    idEl.value = '';
    btnExp.classList.add('active');
    btnInc.classList.remove('active');
  }

  openModal('modalAddExpense');
}

// 8. Form Submission (Add / Edit)
function setupForm() {
  const form = document.getElementById('expenseForm');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const editId = document.getElementById('editExpenseId').value;
    const title = document.getElementById('inputTitle').value.trim();
    const amount = parseFloat(document.getElementById('inputAmount').value);
    const date = document.getElementById('inputDate').value;
    const category = document.getElementById('inputCategory').value;
    const isIncome = document.getElementById('btnTypeIncome').classList.contains('active');
    const type = isIncome ? 'Income' : 'Expense';

    if (!title || isNaN(amount) || amount < 0) {
      alert('Please enter a valid title and amount.');
      return;
    }

    const payload = {
      user_id: editId || String(Date.now()).slice(-6),
      user_title: title,
      user_amount: amount,
      user_catagery: category,
      user_date: date,
      type: type
    };

    try {
      const method = editId ? 'PUT' : 'POST';
      const res = await fetch('/api/transactions', {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!res.ok) throw new Error('Failed to save transaction');

      closeModal('modalAddExpense');
      await loadData();
    } catch (err) {
      alert('Error saving transaction: ' + err.message);
    }
  });
}

// 9. View All Transactions Modal
function openViewAllModal() {
  renderViewAllTable();
  openModal('modalViewExpenses');
}

function renderViewAllTable() {
  const tbody = document.getElementById('viewAllTableBody');
  const countEl = document.getElementById('viewAllCount');
  const filterCat = (document.getElementById('viewFilterCategory').value || 'ALL').toLowerCase();
  const filterType = (document.getElementById('viewFilterType').value || 'ALL').toLowerCase();
  const query = (document.getElementById('viewSearchInput').value || '').toLowerCase().trim();

  if (!tbody) return;
  tbody.innerHTML = '';

  let filtered = allTransactions.filter(tx => {
    const cat = (tx.user_catagery || '').toLowerCase();
    const type = (tx.type || 'Expense').toLowerCase();
    const title = (tx.user_title || '').toLowerCase();
    const id = String(tx.user_id || '').toLowerCase();

    if (filterCat !== 'all' && cat !== filterCat) return false;
    if (filterType !== 'all' && type !== filterType) return false;
    if (query && !title.includes(query) && !id.includes(query) && !cat.includes(query)) return false;
    return true;
  });

  if (countEl) countEl.innerText = filtered.length;

  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding:24px; color:#9ca3af;">No matching transactions found.</td></tr>`;
    return;
  }

  filtered.forEach(tx => {
    const isInc = (tx.type || 'Expense').toLowerCase() === 'income';
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><code>#${escapeHtml(tx.user_id)}</code></td>
      <td>${escapeHtml(tx.user_date || '-')}</td>
      <td><strong>${escapeHtml(tx.user_title || '-')}</strong></td>
      <td><span class="category-pill">${getCategoryEmoji(tx.user_catagery)} ${escapeHtml(tx.user_catagery || 'General')}</span></td>
      <td><span class="type-badge ${isInc ? 'income' : 'expense'}">${isInc ? 'Income' : 'Expense'}</span></td>
      <td style="text-align: right;"><span class="${isInc ? 'amount-income' : 'amount-expense'}">${isInc ? '+' : '-'}${formatINR(tx.user_amount)}</span></td>
      <td style="text-align: center;">
        <button class="btn-secondary" style="padding:4px 8px; font-size:0.75rem; margin-right:4px;" onclick="editTx('${tx.user_id}')">✏️</button>
        <button class="btn-danger" style="padding:4px 8px; font-size:0.75rem;" onclick="deleteTxDirect('${tx.user_id}')">🗑️</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

window.editTx = function(id) {
  const tx = allTransactions.find(t => String(t.user_id) === String(id));
  if (tx) {
    closeModal('modalViewExpenses');
    openAddModal(tx);
  }
};

window.deleteTxDirect = async function(id) {
  if (confirm(`Are you sure you want to delete transaction #${id}?`)) {
    try {
      await fetch(`/api/transactions?id=${id}`, { method: 'DELETE' });
      await loadData();
      renderViewAllTable();
    } catch (err) {
      alert('Delete failed: ' + err.message);
    }
  }
};

// 10. Search Modal
function openSearchModal() {
  const input = document.getElementById('liveSearchInput');
  if (input) {
    input.value = '';
    handleLiveSearch('');
  }
  openModal('modalSearchExpense');
  if (input) setTimeout(() => input.focus(), 150);
}

function handleLiveSearch(query) {
  const list = document.getElementById('searchResultsList');
  if (!list) return;
  const q = (query || '').toLowerCase().trim();

  if (!q) {
    list.innerHTML = `<p class="search-hint">Type above to see matching records instantly.</p>`;
    return;
  }

  const matches = allTransactions.filter(tx => {
    return String(tx.user_id || '').toLowerCase().includes(q) ||
           String(tx.user_title || '').toLowerCase().includes(q) ||
           String(tx.user_catagery || '').toLowerCase().includes(q) ||
           String(tx.user_amount || '').includes(q);
  });

  if (matches.length === 0) {
    list.innerHTML = `<p class="search-hint">No matching transactions found for "${escapeHtml(query)}".</p>`;
    return;
  }

  list.innerHTML = '';
  matches.forEach(tx => {
    const isInc = (tx.type || 'Expense').toLowerCase() === 'income';
    const item = document.createElement('div');
    item.className = 'search-result-item';
    item.innerHTML = `
      <div>
        <strong>#${escapeHtml(tx.user_id)} - ${escapeHtml(tx.user_title)}</strong>
        <span class="category-pill">${getCategoryEmoji(tx.user_catagery)} ${escapeHtml(tx.user_catagery)}</span>
        <div style="font-size:0.8rem; color:#6b7280; margin-top:2px;">Date: ${escapeHtml(tx.user_date || '-')}</div>
      </div>
      <div style="text-align:right;">
        <span class="${isInc ? 'amount-income' : 'amount-expense'}" style="font-size:1.05rem;">
          ${isInc ? '+' : '-'}${formatINR(tx.user_amount)}
        </span>
      </div>
    `;
    list.appendChild(item);
  });
}

// 11. Delete Modal
function openDeleteModal() {
  const select = document.getElementById('deleteSelectId');
  if (select) {
    select.innerHTML = '<option value="">-- Choose Transaction to Delete --</option>';
    allTransactions.forEach(tx => {
      const opt = document.createElement('option');
      opt.value = tx.user_id;
      opt.innerText = `#${tx.user_id} - ${tx.user_title} (${formatINR(tx.user_amount)})`;
      select.appendChild(opt);
    });
  }
  openModal('modalDeleteExpense');
}

async function handleConfirmDelete() {
  const select = document.getElementById('deleteSelectId');
  const id = select ? select.value : '';
  if (!id) {
    alert('Please select a transaction to delete.');
    return;
  }

  if (confirm(`Delete transaction #${id} permanently?`)) {
    try {
      await fetch(`/api/transactions?id=${id}`, { method: 'DELETE' });
      closeModal('modalDeleteExpense');
      await loadData();
    } catch (err) {
      alert('Delete failed: ' + err.message);
    }
  }
}

// 12. Total & Analytics Modal
function openTotalModal() {
  const anaInc = document.getElementById('anaTotalIncome');
  const anaExp = document.getElementById('anaTotalExpense');
  const anaBal = document.getElementById('anaNetBalance');
  const highTitle = document.getElementById('highestTitle');
  const highAmt = document.getElementById('highestAmount');
  const highMeta = document.getElementById('highestMeta');
  const barsWrap = document.getElementById('categoryBarsWrap');

  const inc = analyticsData.total_income || 0;
  const exp = analyticsData.total_expense || 0;
  const bal = analyticsData.balance || 0;

  if (anaInc) anaInc.innerText = formatINR(inc);
  if (anaExp) anaExp.innerText = formatINR(exp);
  if (anaBal) anaBal.innerText = formatINR(bal);

  // Highest Expense
  const high = analyticsData.highest_expense;
  if (high && highTitle && highAmt && highMeta) {
    highTitle.innerText = high.user_title || 'Untitled';
    highAmt.innerText = formatINR(high.user_amount);
    highMeta.innerText = `Category: ${high.user_catagery || 'General'} | Date: ${high.user_date || '-'}`;
  } else if (highTitle) {
    highTitle.innerText = 'No expense recorded yet';
    highAmt.innerText = formatINR(0);
    highMeta.innerText = 'Add expenses to see highlights';
  }

  // Category Breakdown Bars
  if (barsWrap) {
    const breakdown = analyticsData.category_breakdown || {};
    const cats = Object.keys(breakdown);
    if (cats.length === 0) {
      barsWrap.innerHTML = '<p style="color:#9ca3af; font-size:0.85rem;">No expense categories recorded yet.</p>';
    } else {
      barsWrap.innerHTML = '';
      cats.sort((a, b) => breakdown[b] - breakdown[a]).forEach(cat => {
        const catAmt = breakdown[cat];
        const pct = exp > 0 ? Math.round((catAmt / exp) * 100) : 0;
        const row = document.createElement('div');
        row.className = 'category-bar-row';
        row.innerHTML = `
          <div class="cat-bar-header">
            <span>${getCategoryEmoji(cat)} ${escapeHtml(cat)}</span>
            <span>${formatINR(catAmt)} (${pct}%)</span>
          </div>
          <div class="cat-bar-track">
            <div class="cat-bar-fill" style="width: ${pct}%;"></div>
          </div>
        `;
        barsWrap.appendChild(row);
      });
    }
  }

  openModal('modalTotalExpense');
}

// 13. CSV Export
function handleExportCsv() {
  if (!allTransactions || allTransactions.length === 0) {
    alert('No transactions to export.');
    return;
  }
  const headers = ['ID', 'Title', 'Amount', 'Category', 'Date', 'Type'];
  const rows = allTransactions.map(t => [
    t.user_id,
    `"${(t.user_title || '').replace(/"/g, '""')}"`,
    t.user_amount,
    `"${t.user_catagery || ''}"`,
    t.user_date,
    t.type || 'Expense'
  ]);
  const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(e => e.join(','))].join('\n');
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', `Expense_Tracker_Export_${new Date().toISOString().split('T')[0]}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// 14. Exit Handler
function handleExit() {
  if (confirm('Do you want to exit Expense Tracker?')) {
    fetch('/api/exit', { method: 'POST' }).catch(() => {});
    window.close();
    document.body.innerHTML = `
      <div style="color:white; text-align:center; padding:60px; font-family:sans-serif;">
        <h2>👋 Thank You for using Expense Tracker!</h2>
        <p style="color:#a78bfa; margin-top:10px;">You can now close this window.</p>
      </div>
    `;
  }
}

// 15. Windows controls (Min/Max/Close)
function setupWindowControls() {
  const minBtn = document.getElementById('winMinimizeBtn');
  const maxBtn = document.getElementById('winMaximizeBtn');
  const closeBtn = document.getElementById('winCloseBtn');

  if (closeBtn) closeBtn.addEventListener('click', handleExit);
  if (maxBtn) {
    maxBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    });
  }
  if (minBtn) {
    minBtn.addEventListener('click', () => {
      alert('Application minimized. Keep tracking your expenses! 💜');
    });
  }
}
