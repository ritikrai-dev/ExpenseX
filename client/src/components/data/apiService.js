const API = import.meta.env.VITE_API_URL;

const authHeaders = () => ({
    Authorization: `Bearer ${localStorage.getItem("token")}`,
    "Content-Type": "application/json"
});

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

export async function getTransactions(page = 1, limit = 10) {

    const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/transactions?page=${page}&limit=${limit}`,
        {
            headers: {
                Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
        }
    );

    return await response.json();
}

export async function addTransaction(transaction) {

    const res = await fetch(
        `${API}/api/transactions`,
        {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify(transaction),
        }
    );

    return await res.json();
}

export async function updateTransaction(id, transaction) {

    const res = await fetch(
        `${API}/api/transactions/${id}`,
        {
            method: "PUT",
            headers: authHeaders(),
            body: JSON.stringify(transaction),
        }
    );

    return await res.json();
}

export async function deleteTransaction(id) {

    const res = await fetch(
        `${API}/api/transactions/${id}`,
        {
            method: "DELETE",
            headers: authHeaders(),
        }
    );

    return await res.json();
}