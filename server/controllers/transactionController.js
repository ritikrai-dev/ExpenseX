import Transaction from "../models/Transaction.js";

export const addTransaction = async (req, res) => {
  try {
    const {
      type,
      amount,
      category,
      paymentMethod,
      description,
      date,
    } = req.body;

    // Validation
    if (!type || !amount || !category || !paymentMethod) {
      return res.status(400).json({
        success: false,
        message: "Please fill all required fields",
      });
    }
    // Adding Transaction to database
    const transaction = await Transaction.create({
      user: req.user._id,
      type,
      amount,
      category,
      paymentMethod,
      description,
      date,
    });

    return res.status(201).json({
      success: true,
      message: "Transaction added successfully",
      transaction,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// Getting all the transaction of the user
export const getTransactions = async (req, res) => {
  try {
    const transactions = await Transaction.find({
      user: req.user._id,
    }).sort({ createdAt: -1 });

    return res.status(200).json({
      success: true,
      count: transactions.length,
      transactions,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

 
//    Get Single Transaction


export const getTransactionById = async (req, res) => {
  try {
    const transaction = await Transaction.findOne({
      _id: req.params.id,  // this mean the id of the data in thee mongo like id: "6a428b04a5d42b4215dc24ee"
      user: req.user._id, //and this is the user id eg :"user": "6a3e18e84edac40f77e87508"
    });

    if (!transaction) {
      return res.status(404).json({
        success: false,
        message: "Transaction not found",
      });
    }

    return res.status(200).json({
      success: true,
      transaction,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};


//   Update Transaction

export const updateTransaction = async (req, res) => {
  try {
    const transaction = await Transaction.findOne({
      _id: req.params.id,
      user: req.user._id,
    });

    if (!transaction) {
      return res.status(404).json({
        success: false,
        message: "Transaction not found",
      });
    }

    const {
      type,
      amount,
      category,
      paymentMethod,
      description,
      date,
    } = req.body;

    // Updateing  only the fields that are provided
    transaction.type = type || transaction.type;
    transaction.amount = amount || transaction.amount;
    transaction.category = category || transaction.category;
    transaction.paymentMethod =
      paymentMethod || transaction.paymentMethod;
    transaction.description =
      description || transaction.description;
    transaction.date = date || transaction.date;

    const updatedTransaction = await transaction.save();

    return res.status(200).json({
      success: true,
      message: "Transaction updated successfully",
      transaction: updatedTransaction,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};

// Delete Transaction
export const deleteTransaction = async (req, res) => {
  try {
    const transaction = await Transaction.findOne({
      _id: req.params.id,
      user: req.user._id,
    });

    if (!transaction) {
      return res.status(404).json({
        success: false,
        message: "Transaction not found",
      });
    }

    await transaction.deleteOne();

    return res.status(200).json({
      success: true,
      message: "Transaction deleted successfully",
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
};