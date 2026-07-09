import { useEffect, useState } from "react";
import DashboardHeader from "../components/DashboardHeader";
import SummaryCards from "../components/SummaryCards";
import RecentTransactions from "../components/RecentTransactions";

export default function Dashboard() {

    const [dashboardData, setDashboardData] = useState(null);

    useEffect(() => {

        async function fetchDashboard() {

            try {

                const response = await fetch(
                    `${import.meta.env.VITE_API_URL}/api/dashboard`,
                    {
                        headers: {
                            Authorization:
                                `Bearer ${localStorage.getItem("token")}`,
                        },
                    }
                );

                const data = await response.json();

                setDashboardData(data.dashboard);

            } catch (error) {

                console.log(error);

            }

        }

        fetchDashboard();

    }, []);
    
    if (!dashboardData) {

        return <h2>Loading...</h2>;

    }

    return (
        <>
            <DashboardHeader />

            <SummaryCards dashboard={dashboardData} />

            <RecentTransactions
        transactions={dashboardData.recentTransactions}
    />
        </>
    );
}