import { useEffect, useState } from "react";
import DashboardHeader from "../components/DashboardHeader";
import SummaryCards from "../components/SummaryCards";
import RecentTransactions from "../components/RecentTransactions";

import { getDashboard } from "../components/data/demoService";

export default function Dashboard() {

    const [dashboardData, setDashboardData] = useState(null);

    useEffect(() => {

        async function loadDashboard() {

            try {

                const data = await getDashboard();

                setDashboardData(data);

            } catch (error) {

                console.log(error);

            }

        }

        loadDashboard();

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