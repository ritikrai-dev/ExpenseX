import { demoUser, demoTransactions } from "./demoData";

function init() {

    if (!localStorage.getItem("demoUser")) {

        localStorage.setItem(
            "demoUser",
            JSON.stringify(demoUser)
        );
    }

    if (!localStorage.getItem("demoTransactions")) {

        localStorage.setItem(
            "demoTransactions",
            JSON.stringify(demoTransactions)
        );
    }
}

init();

export function getUser() {

    return JSON.parse(localStorage.getItem("demoUser"));
}

export function getTransactions() {

    return JSON.parse(
        localStorage.getItem("demoTransactions")
    ) || [];
}

function saveTransactions(data) {

    localStorage.setItem(
        "demoTransactions",
        JSON.stringify(data)
    );
}

export function addTransaction(transaction) {

    const transactions = getTransactions();

    const newTransaction = {

        ...transaction,

        _id: crypto.randomUUID(),

        createdAt: new Date().toISOString(),

    };

    transactions.unshift(newTransaction);

    saveTransactions(transactions);

    return {

        success: true,

        transaction: newTransaction,

    };
}

export function updateTransaction(id, data) {

    const updated = getTransactions().map((transaction) =>

        transaction._id === id

            ? { ...transaction, ...data }

            : transaction
    );

    saveTransactions(updated);

    return {

        success: true,

    };
}

export function deleteTransaction(id) {

    const filtered = getTransactions().filter(

        transaction => transaction._id !== id

    );

    saveTransactions(filtered);

    return {

        success: true,

    };
}

export function getDashboard() {

    const transactions = getTransactions();

    const income = transactions

        .filter(transaction =>

            transaction.type.toLowerCase() === "income"

        )

        .reduce(

            (sum, transaction) =>

                sum + Number(transaction.amount),

            0

        );

    const expense = transactions

        .filter(transaction =>

            transaction.type.toLowerCase() === "expense"

        )

        .reduce(

            (sum, transaction) =>

                sum + Number(transaction.amount),

            0

        );

    return {

        balance: income - expense,

        totalIncome: income,

        totalExpense: expense,

        totalTransactions: transactions.length,

        recentTransactions: [...transactions]

            .reverse()

            .slice(0,5),

    };
}