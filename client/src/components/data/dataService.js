import * as api from "./apiService";
import * as demo from "./demoService";


const isDemo = () => {

    const demoMode =
        localStorage.getItem("demoMode");


    const token =
        localStorage.getItem("token");


    return demoMode === "true" && !token;

};





export function getDashboard() {

    if(isDemo()) {

        return Promise.resolve(
            demo.getDashboard()
        );

    }


    return api.getDashboard();

}





export function getUser() {


    if(isDemo()) {

        return Promise.resolve(
            demo.getUser()
        );

    }


    return api.getUser();

}





export async function getTransactions() {


    if(isDemo()) {

        return demo.getTransactions();

    }


    const data =
    await api.getTransactions();


    return data.transactions || [];

}





export function addTransaction(transaction) {


    if(isDemo()) {

        return Promise.resolve(
            demo.addTransaction(transaction)
        );

    }


    return api.addTransaction(transaction);

}





export function updateTransaction(id,data) {


    if(isDemo()) {

        return Promise.resolve(
            demo.updateTransaction(id,data)
        );

    }


    return api.updateTransaction(id,data);

}





export function deleteTransaction(id) {


    if(isDemo()) {

        return Promise.resolve(
            demo.deleteTransaction(id)
        );

    }


    return api.deleteTransaction(id);

}