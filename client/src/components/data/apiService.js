export async function getDashboard() {

    const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/dashboard`,
        {
            headers: {
                Authorization:
                    `Bearer ${localStorage.getItem("token")}`
            }
        }
    );

    const data = await response.json();

    return data.dashboard;
}