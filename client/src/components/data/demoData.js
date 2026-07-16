export const demoUser = {
  id: "guest-user",
  name: "Guest User",
  email: "guest@expensex.demo",
};

export const demoTransactions = [
  {
    _id: crypto.randomUUID(),
    type: "Income",
    category: "Salary",
    amount: 50000,
    note: "Monthly Salary",
    date: "2026-07-01",
  },
  {
    _id: crypto.randomUUID(),
    type: "Expense",
    category: "Food",
    amount: 420,
    note: "Lunch",
    date: "2026-07-04",
  },
  {
    _id: crypto.randomUUID(),
    type: "Expense",
    category: "Shopping",
    amount: 2100,
    note: "Shoes",
    date: "2026-07-08",
  },
  {
    _id: crypto.randomUUID(),
    type: "Expense",
    category: "Travel",
    amount: 800,
    note: "Metro Card",
    date: "2026-07-10",
  },
];