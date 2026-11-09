import * as api from "./apiService";
import * as demo from "./demoService";

export const isDemo = () => {
  const demoMode = localStorage.getItem("demoMode");
  const token = localStorage.getItem("token");
  return demoMode === "true" || !token;
};

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

export async function updateUser(profile) {
  if (isDemo()) {
    return demo.updateUser(profile);
  }
  return api.updateUser(profile);
}

export async function changePassword(passwords) {
  if (isDemo()) {
    return demo.changePassword(passwords);
  }
  return api.changePassword(passwords);
}

export async function getTransactions(page = 1, limit = 10) {
  if (isDemo()) {
    const all = demo.getTransactions();
    return all;
  }
  const data = await api.getTransactions(page, limit);
  return data.transactions || data || [];
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

export async function getCategoryAnalytics() {
  if (isDemo()) {
    return demo.getCategoryAnalytics();
  }
  return api.getCategoryAnalytics();
}

export async function getMonthlyExpense() {
  if (isDemo()) {
    return demo.getMonthlyExpense();
  }
  return api.getMonthlyExpense();
}

export async function getAIInsights() {
  if (isDemo()) {
    return demo.getAIInsights();
  }
  return api.getAIInsights();
}

export async function downloadReport(type = "pdf", filterDate = false, fromDate = "", toDate = "") {
  if (isDemo()) {
    return demo.downloadReport(type, filterDate, fromDate, toDate);
  }
  return api.downloadReport(type, filterDate, fromDate, toDate);
}