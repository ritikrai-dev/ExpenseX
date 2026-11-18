import { useEffect, useState } from "react";
import ReportSummary from "../components/ReportSummary.jsx";
import { getDashboard, downloadReport } from "../components/data/dataService";
import { toast } from "react-toastify";
import "../style/report.css";

export default function Reports() {
  const [summary, setSummary] = useState({
    totalIncome: 0,
    totalExpense: 0,
    balance: 0,
    totalTransactions: 0,
  });
  const [fromDate, setFromDate] = useState("");
  const [toDate, setToDate] = useState("");
  const [downloading, setDownloading] = useState(false);

  async function fetchSummary() {
    try {
      const data = await getDashboard();
      if (data) {
        setSummary({
          totalIncome: data.totalIncome || 0,
          totalExpense: data.totalExpense || 0,
          balance: data.balance || 0,
          totalTransactions: data.totalTransactions || 0,
        });
      }
    } catch (error) {
      console.error("Fetch Summary Error:", error);
    }
  }

  useEffect(() => {
    fetchSummary();
  }, []);

  const handleDownload = async (type, filterDate = false) => {
    if (filterDate && (!fromDate || !toDate)) {
      toast.warning("Please choose both From and To dates.");
      return;
    }
    try {
      setDownloading(true);
      await downloadReport(type, filterDate, fromDate, toDate);
      toast.success(`${type.toUpperCase()} report generated!`);
    } catch (error) {
      console.error(error);
      toast.error("Failed to download report.");
    } finally {
      setDownloading(false);
    }
  };

  return (
    <>
      <h1 className="page-title">Reports</h1>

      <ReportSummary summary={summary} />

      {/* Complete Report Export */}
      <div className="export-section">
        <h2 className="export-title">Export Financial Reports</h2>
        <p className="export-subtitle">
          Download your complete expense history in standard file formats.
        </p>

        <div className="report-actions">
          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("pdf")}
          >
            📄 Export PDF
          </button>

          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("excel")}
          >
            📊 Export Excel
          </button>

          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("csv")}
          >
            📑 Export CSV
          </button>

          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("json")}
          >
            💾 Export JSON
          </button>
        </div>
      </div>

      {/* Date Based Report */}
      <div className="export-section date-report-section">
        <h2 className="export-title">Download Report By Date Range</h2>
        <p className="export-subtitle">
          Select date range and download filtered transactions.
        </p>

        <div className="date-filter">
          <div>
            <label>From Date</label>
            <input
              type="date"
              value={fromDate}
              onChange={(e) => setFromDate(e.target.value)}
            />
          </div>

          <div>
            <label>To Date</label>
            <input
              type="date"
              value={toDate}
              onChange={(e) => setToDate(e.target.value)}
            />
          </div>
        </div>

        <div className="report-actions">
          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("pdf", true)}
          >
            📄 Download Filtered PDF
          </button>

          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("excel", true)}
          >
            📊 Download Filtered Excel
          </button>

          <button
            className="primary-btn"
            disabled={downloading}
            onClick={() => handleDownload("csv", true)}
          >
            📑 Download Filtered CSV
          </button>
        </div>
      </div>
    </>
  );
}