import { useEffect, useState } from "react";
import DashboardHeader from "../components/DashboardHeader";
import SummaryCards from "../components/SummaryCards";
import BarGraph from "../components/landing/BarGraph.jsx";

import { getDashboard } from "../components/data/dataService";

export default function Dashboard() {
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true);

        const dashboard = await getDashboard();

        setDashboardData(dashboard);
      } catch (error) {
        console.error("Dashboard Error:", error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (!dashboardData) {
    return <h2>Failed to load dashboard.</h2>;
  }

  return (
    <>
      <DashboardHeader />

      <SummaryCards dashboard={dashboardData} />

      <BarGraph
 transactions={
   dashboardData.recentTransactions ||
   []
 }
/>
    </>
  );
}