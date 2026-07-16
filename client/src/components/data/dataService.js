import * as demo from "./demoService";
import * as api from "./apiService";

const isDemo =
    () => localStorage.getItem("demoMode") === "true";

export async function getDashboard() {

    if (isDemo()) {
        return demo.getDashboard();
    }

    return api.getDashboard();
}

export async function getUser() {

    if (isDemo()) {
        return demo.getUser();
    }

    return api.getUser();
}

export async function addTransaction(transaction) {

    if (isDemo()) {
        return demo.addTransaction(transaction);
    }

    return api.addTransaction(transaction);
}

export async function updateTransaction(id, data) {

    if (isDemo()) {
        return demo.updateTransaction(id, data);
    }

    return api.updateTransaction(id, data);
}

export async function deleteTransaction(id) {

    if (isDemo()) {
        return demo.deleteTransaction(id);
    }

    return api.deleteTransaction(id);
}

export async function getTransactions() {

    if (isDemo()) {
        return demo.getTransactions();
    }

    return api.getTransactions();
}