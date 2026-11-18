# 👛 Expense Tracker Application (StudySync / Urvashi Edition)

Modern pastel desktop application for tracking expenses and income, designed with the custom purple theme.

![Expense Tracker](web/index.html)

## ✨ Features
1. **🎨 Exact Custom UI**:
   - Deep indigo/midnight purple sidebar with 3D wallet logo, gold coins, sparkles, and botanical quote.
   - 3 Pastel Summary Cards: **Total Income** (Mint Green), **Total Expense** (Blush Pink), **Balance** (Lavender).
   - **Expense Overview**: Live dual-line / bar Canvas chart tracking Income & Expenses across 12 months (Jan–Dec).
   - **Cute Motivation Card**: Sprouting gold coin jar with quote *"Small steps make a big difference! ♡"*.
   - **Recent Transactions**: Interactive table with category pills, income/expense tags, and instant empty-state design.

2. **⚡ Fully Interactive Modals**:
   - `+ Add Expense`: Add income or expense with category icons, date picker, amount, and notes.
   - `👁 View Expense`: Filter by type, month, or category, with live search and CSV export.
   - `🔍 Search Expense`: Live instant lookup by ID, title, or category.
   - `🗑 Delete Expense`: Delete transaction with confirmation.
   - `📈 Total Expense`: Visual category spending progress bars and highest expense highlight.
   - `🚪 Exit`: Graceful shutdown.

3. **💾 Shared Data Persistence**:
   - Saves to `expence.json` in the same directory.
   - 100% backward compatible with original CLI files (`load_expences.py`, `save_expences.py`, `add_expences.py`, etc.).

---

## 🚀 How to Run

### 1. Launch the Desktop Application (Default)
Double-click `run_app.bat` or run:
```bash
python main.py
```
*Automatically launches as a dedicated desktop application window on Windows!*

### 2. Run in CLI Terminal Mode
If you prefer the original interactive terminal menu:
```bash
python main.py --cli
```
