import { useEffect, useState } from "react";
import AIInsightCard from "../components/AIInsightCard";
import { getAIInsights } from "../components/data/dataService";

export default function AIInsights() {
  const [insights, setInsights] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchInsights();
  }, []);

  const fetchInsights = async () => {
    try {
      setLoading(true);
      const data = await getAIInsights();
      setInsights(data);
    } catch (error) {
      console.error("AI Insights Error:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          minHeight: "60vh",
          fontSize: "22px",
          fontWeight: "600",
        }}
      >
        🤖 Generating AI Insights...
      </div>
    );
  }

  if (!insights) {
    return (
      <div className="chart-card">
        <h2>No AI insights available.</h2>
        <p>Try refreshing after adding some transactions.</p>
        <button className="primary-btn" onClick={fetchInsights} style={{ marginTop: "1rem" }}>
          Retry
        </button>
      </div>
    );
  }

  return (
    <>
      <div className="page-header">
        <h1>🤖 AI Financial Insights</h1>
        <button className="primary-btn" onClick={fetchInsights}>
          Refresh
        </button>
      </div>
      <AIInsightCard insights={insights} />
    </>
  );
}