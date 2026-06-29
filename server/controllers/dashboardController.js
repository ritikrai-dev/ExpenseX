import Transaction from "../models/Transaction.js";

export const getDashboard = async (req, res) => {
  try {
    // Get all transactions of the logged-in user
    const transactions = await Transaction.find({
      user: req.user._id,
    }).sort({ createdAt: -1 });

    let totalIncome = 0;
    let totalExpense = 0;

    transactions.forEach((transaction) => {
      if (transaction.type === "income") {
        totalIncome += transaction.amount;
      } else {
        totalExpense += transaction.amount;
      }
    });

    const balance = totalIncome - totalExpense;

    const recentTransactions = transactions.slice(0, 5); //give lates 5 transaction 

    return res.status(200).json({
      success: true,
      dashboard: {
        balance,
        totalIncome,
        totalExpense,
        totalTransactions: transactions.length,
        recentTransactions,
      },
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

