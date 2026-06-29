import Transaction from "../models/Transaction.js";

//   Category Wise Expense Analytics

export const getCategoryAnalytics = async (req, res) => {
  try {
    const transactions = await Transaction.find({
      user: req.user._id,
    });

    const categoryData = {};

    transactions.forEach((transaction) => {
      if (transaction.type === "expense") {
        if (categoryData[transaction.category]) {
          categoryData[transaction.category] += transaction.amount;
        } else {
          categoryData[transaction.category] = transaction.amount;
        }
      }
    });

    return res.status(200).json({
      success: true,
      categoryData,
    });

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

//    Monthly Expense Trend

export const getMonthlyExpense = async (req, res) => {
  try {
    const transactions = await Transaction.find({
      user: req.user._id,
      type: "expense",
    });

    const monthlyData = {};

    const months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];

    transactions.forEach((transaction) => {
      const date = new Date(transaction.date);

      const month = months[date.getMonth()];

      if (monthlyData[month]) {
        monthlyData[month] += transaction.amount;
      } else {
        monthlyData[month] = transaction.amount;
      }
    });

    // Convert object into array
    const monthlyExpense = Object.keys(monthlyData).map((month) => ({
      month,
      amount: monthlyData[month],
    }));

    return res.status(200).json({
      success: true,
      monthlyExpense,
    });

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};