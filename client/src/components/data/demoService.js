import { demoUser, demoTransactions } from "./demoData";

function initializeDemo() {

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

initializeDemo();

export function getUser() {
    return JSON.parse(localStorage.getItem("demoUser"));
}

export function getTransactions() {
    return JSON.parse(localStorage.getItem("demoTransactions")) || [];
}

export function saveTransactions(data) {
    localStorage.setItem(
        "demoTransactions",
        JSON.stringify(data)
    );
}
export function addTransaction(transaction) {

    const transactions = getTransactions();

    const newTransaction = {
        _id: Date.now().toString(),
        ...transaction,
        createdAt: new Date().toISOString()
    };

    transactions.unshift(newTransaction);

    saveTransactions(transactions);

    return newTransaction;
}

export function updateTransaction(id, updatedData) {

    const transactions = getTransactions();

    const updated = transactions.map(transaction =>
        transaction._id === id
            ? { ...transaction, ...updatedData }
            : transaction
    );

    saveTransactions(updated);
}

export function deleteTransaction(id) {

    const transactions = getTransactions();

    const filtered = transactions.filter(
        transaction => transaction._id !== id
    );

    saveTransactions(filtered);
}

export function getDashboard() {

    const transactions = getTransactions();

    const totalIncome = transactions
        .filter(t => t.type === "income")
        .reduce((sum, t) => sum + Number(t.amount), 0);

    const totalExpense = transactions
        .filter(t => t.type === "expense")
        .reduce((sum, t) => sum + Number(t.amount), 0);

    return {

        balance: totalIncome - totalExpense,

        totalIncome,

        totalExpense,

        totalTransactions: transactions.length,

        recentTransactions: [...transactions]
            .reverse()
            .slice(0, 5)

    };

}