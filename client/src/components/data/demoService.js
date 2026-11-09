import { demoUser, demoTransactions } from "./demoData";

export function initDemoData(force = false) {
  if (force || !localStorage.getItem("demoUser")) {
    localStorage.setItem("demoUser", JSON.stringify(demoUser));
  }

  const existingTxs = localStorage.getItem("demoTransactions");
  if (force || !existingTxs || JSON.parse(existingTxs).length === 0) {
    localStorage.setItem(
      "demoTransactions",
      JSON.stringify(demoTransactions)
    );
  }
}

export function enableDemoMode() {
  initDemoData();
  localStorage.setItem("demoMode", "true");
  localStorage.removeItem("token");
}

export function getUser() {
  initDemoData();
  try {
    const raw = localStorage.getItem("demoUser");
    return raw ? JSON.parse(raw) : demoUser;
  } catch {
    return demoUser;
  }
}

export function updateUser(profile) {
  initDemoData();
  const current = getUser();
  const updated = {
    ...current,
    name: profile.name || current.name,
    email: profile.email || current.email,
  };
  localStorage.setItem("demoUser", JSON.stringify(updated));
  localStorage.setItem("user", JSON.stringify(updated));
  return {
    success: true,
    message: "Profile updated successfully (Guest Mode)",
    user: updated,
  };
}

export function changePassword(passwords) {
  if (!passwords.currentPassword || !passwords.newPassword || !passwords.confirmPassword) {
    return {
      success: false,
      message: "All fields are required.",
    };
  }
  if (passwords.newPassword !== passwords.confirmPassword) {
    return {
      success: false,
      message: "Passwords do not match.",
    };
  }
  return {
    success: true,
    message: "Password updated successfully in Guest session.",
  };
}

export function getTransactions() {
  initDemoData();
  try {
    const raw = localStorage.getItem("demoTransactions");
    return raw ? JSON.parse(raw) : demoTransactions;
  } catch {
    return demoTransactions;
  }
}

function saveTransactions(data) {
  localStorage.setItem("demoTransactions", JSON.stringify(data));
}

export function addTransaction(transaction) {
  const transactions = getTransactions();

  const newTransaction = {
    ...transaction,
    _id: typeof crypto !== "undefined" && crypto.randomUUID ? crypto.randomUUID() : `tx-${Date.now()}`,
    amount: Number(transaction.amount) || 0,
    type: (transaction.type || "expense").toLowerCase(),
    category: transaction.category || "General",
    paymentMethod: transaction.paymentMethod || "Cash",
    description: transaction.description || "",
    date: transaction.date || new Date().toISOString().split("T")[0],
    createdAt: new Date().toISOString(),
  };

  transactions.unshift(newTransaction);
  saveTransactions(transactions);

  return {
    success: true,
    message: "Transaction added successfully",
    transaction: newTransaction,
  };
}

export function updateTransaction(id, data) {
  const transactions = getTransactions();
  let updatedTransaction = null;

  const updated = transactions.map((t) => {
    if (t._id === id) {
      updatedTransaction = {
        ...t,
        ...data,
        amount: data.amount ? Number(data.amount) : t.amount,
        type: data.type ? data.type.toLowerCase() : t.type,
      };
      return updatedTransaction;
    }
    return t;
  });

  saveTransactions(updated);

  return {
    success: true,
    message: "Transaction updated successfully",
    transaction: updatedTransaction || { ...data, _id: id },
  };
}

export function deleteTransaction(id) {
  const transactions = getTransactions();
  const filtered = transactions.filter((t) => t._id !== id);
  saveTransactions(filtered);

  return {
    success: true,
    message: "Transaction deleted successfully",
  };
}

export function getDashboard() {
  const transactions = getTransactions();

  let income = 0;
  let expense = 0;

  transactions.forEach((t) => {
    const amt = Number(t.amount) || 0;
    if (t.type?.toLowerCase() === "income") {
      income += amt;
    } else {
      expense += amt;
    }
  });

  return {
    balance: income - expense,
    totalIncome: income,
    totalExpense: expense,
    totalTransactions: transactions.length,
    recentTransactions: transactions.slice(0, 5),
  };
}

export function getCategoryAnalytics() {
  const transactions = getTransactions();
  const categoryData = {};

  transactions.forEach((t) => {
    if (t.type?.toLowerCase() === "expense") {
      const cat = t.category || "General";
      categoryData[cat] = (categoryData[cat] || 0) + (Number(t.amount) || 0);
    }
  });

  return {
    success: true,
    categoryData,
  };
}

export function getMonthlyExpense() {
  const transactions = getTransactions();
  const monthlyData = {};

  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];

  transactions.forEach((t) => {
    if (t.type?.toLowerCase() === "expense") {
      const d = new Date(t.date || t.createdAt);
      if (!isNaN(d.getTime())) {
        const monthName = months[d.getMonth()];
        monthlyData[monthName] = (monthlyData[monthName] || 0) + (Number(t.amount) || 0);
      }
    }
  });

  const monthlyExpense = Object.keys(monthlyData).map((month) => ({
    month,
    amount: monthlyData[month],
  }));

  // Sort chronologically by calendar month index
  monthlyExpense.sort((a, b) => months.indexOf(a.month) - months.indexOf(b.month));

  return {
    success: true,
    monthlyExpense: monthlyExpense.length > 0 ? monthlyExpense : [{ month: "Current", amount: 0 }],
  };
}

export function getAIInsights() {
  const transactions = getTransactions();
  let income = 0;
  let expense = 0;
  const categoryTotals = {};

  transactions.forEach((t) => {
    const amt = Number(t.amount) || 0;
    if (t.type?.toLowerCase() === "income") {
      income += amt;
    } else {
      expense += amt;
      const cat = t.category || "General";
      categoryTotals[cat] = (categoryTotals[cat] || 0) + amt;
    }
  });

  const balance = income - expense;
  let highestCat = "None";
  let highestAmt = 0;

  for (const [cat, amt] of Object.entries(categoryTotals)) {
    if (amt > highestAmt) {
      highestAmt = amt;
      highestCat = cat;
    }
  }

  const savingsRate = income > 0 ? Math.max(0, Math.round((balance / income) * 100)) : 0;
  const score = Math.min(100, Math.max(25, Math.round(savingsRate * 0.7 + (highestAmt / (expense || 1) < 0.4 ? 30 : 15))));

  let health = "Good";
  if (score >= 80) health = "Excellent";
  else if (score >= 60) health = "Stable / Healthy";
  else if (score >= 40) health = "Moderate Risk";
  else health = "Needs Attention";

  return {
    financialHealth: health,
    score,
    spendingAnalysis: `In your guest session, total recorded earnings stand at ₹${income.toLocaleString()} against expenditures of ₹${expense.toLocaleString()}, yielding a net balance of ₹${balance.toLocaleString()} (${savingsRate}% savings rate).`,
    savingsRecommendation: `Optimizing your ${highestCat !== "None" ? highestCat : "discretionary"} spending by 10% would allocate approximately ₹${Math.round((highestAmt || 1000) * 0.1).toLocaleString()} toward your emergency reserve fund.`,
    highestExpenseCategory: highestCat,
    highestExpenseAmount: highestAmt,
    smartAlerts: [
      highestAmt > 0
        ? `Primary outflow: ${highestCat} constitutes ${Math.round((highestAmt / (expense || 1)) * 100)}% of your total recorded expenses.`
        : "Record routine transactions to detect category concentration.",
      balance >= 0
        ? `Positive net balance of ₹${balance.toLocaleString()} maintained.`
        : "Warning: Recorded expenses currently exceed total reported income.",
    ],
    personalizedTips: [
      "Follow the 50/30/20 guideline: 50% for core needs, 30% for lifestyle wants, and 20% dedicated to savings.",
      "Track recurring digital micropayments to prevent invisible budget leakage.",
      "Register a permanent account to synchronize your financial records securely in MongoDB Atlas."
    ],
    nextMonthGoal: `Target a net savings benchmark of ₹${Math.max(5000, Math.round(balance * 1.15)).toLocaleString()} for next month.`,
  };
}

export function downloadReport(type = "pdf", filterDate = false, fromDate = "", toDate = "") {
  let txs = getTransactions();

  if (filterDate && fromDate && toDate) {
    const from = new Date(fromDate).getTime();
    const to = new Date(toDate).getTime();
    txs = txs.filter((t) => {
      const d = new Date(t.date || t.createdAt).getTime();
      return d >= from && d <= to;
    });
  }

  const income = txs.filter((t) => t.type?.toLowerCase() === "income").reduce((s, t) => s + Number(t.amount), 0);
  const expense = txs.filter((t) => t.type?.toLowerCase() === "expense").reduce((s, t) => s + Number(t.amount), 0);
  const balance = income - expense;

  if (type === "csv") {
    let csv = "Type,Amount,Category,Payment Method,Description,Date\n";
    txs.forEach((t) => {
      csv += `"${t.type}","${t.amount}","${t.category}","${t.paymentMethod || ""}","${(t.description || "").replace(/"/g, '""')}","${t.date}"\n`;
    });
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    triggerDownload(blob, "expense-report-guest.csv");
    return;
  }

  if (type === "json") {
    const report = {
      generatedAt: new Date().toISOString(),
      user: "Guest User",
      totalTransactions: txs.length,
      summary: { totalIncome: income, totalExpense: expense, balance },
      transactions: txs,
    };
    const blob = new Blob([JSON.stringify(report, null, 2)], { type: "application/json" });
    triggerDownload(blob, "expense-report-guest.json");
    return;
  }

  if (type === "excel") {
    // Generate CSV with Excel UTF-8 BOM so Excel opens it with proper columns
    let csv = "\uFEFFType,Amount (INR),Category,Payment Method,Description,Date\n";
    txs.forEach((t) => {
      csv += `"${t.type.toUpperCase()}",${t.amount},"${t.category}","${t.paymentMethod || ""}","${(t.description || "").replace(/"/g, '""')}","${t.date}"\n`;
    });
    csv += `\n"SUMMARY","","","","",""\n`;
    csv += `"Total Income",${income},"","","",""\n`;
    csv += `"Total Expense",${expense},"","","",""\n`;
    csv += `"Net Balance",${balance},"","","",""\n`;

    const blob = new Blob([csv], { type: "application/vnd.ms-excel;charset=utf-8;" });
    triggerDownload(blob, "expense-report-guest.xlsx");
    return;
  }

  // Default: Formatted Statement / PDF-like text document
  let docContent = "========================================================\n";
  docContent += "             EXPENSEX FINANCIAL STATEMENT (GUEST)      \n";
  docContent += "========================================================\n\n";
  docContent += `Generated On  : ${new Date().toLocaleString()}\n`;
  docContent += `Account       : Guest User (Demo Session)\n`;
  docContent += `Total Income  : ₹${income.toLocaleString()}\n`;
  docContent += `Total Expense : ₹${expense.toLocaleString()}\n`;
  docContent += `Current Balance: ₹${balance.toLocaleString()}\n`;
  docContent += `Total Records : ${txs.length}\n`;
  docContent += "--------------------------------------------------------\n";
  docContent += "TRANSACTION DETAILS:\n";
  docContent += "--------------------------------------------------------\n\n";

  txs.forEach((t, i) => {
    docContent += `${i + 1}. [${t.type.toUpperCase()}] ₹${Number(t.amount).toLocaleString()}\n`;
    docContent += `   Category : ${t.category}\n`;
    docContent += `   Payment  : ${t.paymentMethod || "N/A"}\n`;
    docContent += `   Date     : ${t.date}\n`;
    docContent += `   Note     : ${t.description || "-"}\n\n`;
  });

  docContent += "========================================================\n";
  docContent += "ExpenseX Smart Expense Tracker | https://expensex.demo\n";

  const blob = new Blob([docContent], { type: "text/plain;charset=utf-8;" });
  triggerDownload(blob, "expense-report-guest.txt");
}

function triggerDownload(blob, filename) {
  const fileUrl = window.URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = fileUrl;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.URL.revokeObjectURL(fileUrl);
}