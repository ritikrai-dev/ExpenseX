import * as api from "./apiService";
import * as demo from "./demoService";

const isDemo = () => {
    const token = localStorage.getItem("token");
    const demo = localStorage.getItem("demoMode");

    return !token && demo === "true";
};

export function getDashboard() {

    return isDemo()

        ? Promise.resolve(demo.getDashboard())

        : api.getDashboard();
}

export function getUser() {

    return isDemo()

        ? Promise.resolve(demo.getUser())

        : api.getUser();
}

export async function getTransactions() {
    if (isDemo()) {
        return demo.getTransactions();
    }

    const data = await api.getTransactions();

    return data.transactions;
}

export function addTransaction(transaction) {

    return isDemo()

        ? Promise.resolve(

              demo.addTransaction(transaction)

          )

        : api.addTransaction(transaction);
}

export function updateTransaction(id, data) {

    return isDemo()

        ? Promise.resolve(

              demo.updateTransaction(id, data)

          )

        : api.updateTransaction(id, data);
}

export function deleteTransaction(id) {

    return isDemo()

        ? Promise.resolve(

              demo.deleteTransaction(id)

          )

        : api.deleteTransaction(id);
}