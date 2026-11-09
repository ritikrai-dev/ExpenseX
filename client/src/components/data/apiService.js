const API = import.meta.env.VITE_API_URL;

const authHeaders = () => {
  const token = localStorage.getItem("token");
  return {
    ...(token && {
      Authorization: `Bearer ${token}`,
    }),
    "Content-Type": "application/json",
  };
};

export async function getDashboard() {
  const res = await fetch(`${API}/api/dashboard`, {
    headers: authHeaders(),
  });
  const data = await res.json();
  return data.dashboard;
}

export async function getUser() {
  const res = await fetch(`${API}/api/users/profile`, {
    headers: authHeaders(),
  });
  const data = await res.json();
  return data.user;
}

export async function updateUser(profile) {
  const res = await fetch(`${API}/api/users/profile`, {
    method: "PUT",
    headers: authHeaders(),
    body: JSON.stringify(profile),
  });
  return await res.json();
}

export async function changePassword(passwords) {
  const res = await fetch(`${API}/api/users/change-password`, {
    method: "PUT",
    headers: authHeaders(),
    body: JSON.stringify(passwords),
  });
  return await res.json();
}

export async function getTransactions(page = 1, limit = 10) {
  const response = await fetch(
    `${API}/api/transactions?page=${page}&limit=${limit}`,
    {
      headers: authHeaders(),
    }
  );
  return await response.json();
}

export async function addTransaction(transaction) {
  const res = await fetch(`${API}/api/transactions`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(transaction),
  });
  return await res.json();
}

export async function updateTransaction(id, transaction) {
  const res = await fetch(`${API}/api/transactions/${id}`, {
    method: "PUT",
    headers: authHeaders(),
    body: JSON.stringify(transaction),
  });
  return await res.json();
}

export async function deleteTransaction(id) {
  const res = await fetch(`${API}/api/transactions/${id}`, {
    method: "DELETE",
    headers: authHeaders(),
  });
  return await res.json();
}

export async function getCategoryAnalytics() {
  const res = await fetch(`${API}/api/analytics/category`, {
    headers: authHeaders(),
  });
  return await res.json();
}

export async function getMonthlyExpense() {
  const res = await fetch(`${API}/api/analytics/monthly-expense`, {
    headers: authHeaders(),
  });
  return await res.json();
}

export async function getAIInsights() {
  const res = await fetch(`${API}/api/ai/insights`, {
    headers: authHeaders(),
  });
  const data = await res.json();
  return data.insights;
}

export async function downloadReport(type = "pdf", filterDate = false, fromDate = "", toDate = "") {
  let url = `${API}/api/reports/${type}`;
  if (filterDate && fromDate && toDate) {
    url += `?fromDate=${fromDate}&toDate=${toDate}`;
  }

  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });

  if (!response.ok) {
    throw new Error("Download failed");
  }

  const blob = await response.blob();
  const fileUrl = window.URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = fileUrl;
  link.download = `expense-report.${type === "excel" ? "xlsx" : type}`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.URL.revokeObjectURL(fileUrl);
}