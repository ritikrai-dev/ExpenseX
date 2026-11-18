import { useEffect, useState } from "react";
import ExpenseCategoryChart from "../components/ExpenseCategoryChart.jsx";
import MonthlyExpenseChart from "../components/MonthlyExpenseChart.jsx";
import {
  getCategoryAnalytics,
  getMonthlyExpense,
  getTransactions,
} from "../components/data/dataService";
import "../style/analytics.css";

export default function Analytics() {
  const [categoryData, setCategoryData] = useState([]);
  const [monthlyData, setMonthlyData] = useState([]);
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadAllData() {
      try {
        setLoading(true);
        await Promise.all([fetchCategory(), fetchMonthly(), fetchTransactions()]);
      } finally {
        setLoading(false);
      }
    }
    loadAllData();
  }, []);

  async function fetchCategory() {
    try {
      const data = await getCategoryAnalytics();
      const rawCategories = data?.categoryData || {};
      const formatted = Object.entries(rawCategories).map(([name, value]) => ({
        name,
        value: Number(value) || 0,
      }));
      setCategoryData(formatted);
    } catch (error) {
      console.error("Category Analytics Error:", error);
    }
  }

  async function fetchMonthly() {
    try {
      const data = await getMonthlyExpense();
      setMonthlyData(data?.monthlyExpense || []);
    } catch (error) {
      console.error("Monthly Analytics Error:", error);
    }
  }

  async function fetchTransactions() {
    try {
      const data = await getTransactions();
      const txs = Array.isArray(data) ? data : (data?.transactions || []);
      setTransactions(txs);
    } catch (error) {
      console.error("Transaction Error:", error);
    }
  }

  return (
    <div className="analytics-container">
      {loading ? (
        <h2>Loading analytics...</h2>
      ) : (
        <div className="analytics-grid">
          <div className="analytics-card-wrapper">
            <ExpenseCategoryChart
              data={categoryData}
              transactions={transactions}
            />
          </div>
          <div className="analytics-card-wrapper">
            <MonthlyExpenseChart data={monthlyData} />
          </div>
        </div>
      )}
    </div>
  );
}