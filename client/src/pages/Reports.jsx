import ReportSummary from "../components/ReportSummary.jsx";
import { useEffect, useState } from "react";

export default function Reports() {
    const [summary, setSummary] = useState({
    totalIncome:0,
    totalExpense:0,
    balance:0,
    totalTransactions:0
});
async function fetchSummary(){

    try{

        const response = await fetch(

            `${import.meta.env.VITE_API_URL}/api/dashboard`,

            {

                headers:{

                    Authorization:`Bearer ${localStorage.getItem("token")}`

                }

            }

        );

        const data = await response.json();

        setSummary({

            totalIncome:data.dashboard.totalIncome,

            totalExpense:data.dashboard.totalExpense,

            balance:data.dashboard.balance,

            totalTransactions:data.dashboard.totalTransactions

        });

    }

    catch(error){

        console.log(error);

    }

}

useEffect(() => {
    fetchSummary();
}, []);
    const downloadReport = async (type) => {

    try {

        const response = await fetch(

            `${import.meta.env.VITE_API_URL}/api/reports/${type}`,

            {

                headers: {

                    Authorization: `Bearer ${localStorage.getItem("token")}`

                }

            }

        );

        if (!response.ok) {

            throw new Error("Download failed");

        }

        const blob = await response.blob();

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = `expense-report.${type === "excel" ? "xlsx" : type}`;

        document.body.appendChild(link);

        link.click();

        link.remove();

        window.URL.revokeObjectURL(url);

    }

    catch (error) {

        console.log(error);

    }

};

    return (

        <>

            <h1 className="page-title">
                Reports
            </h1>
            <ReportSummary summary={summary} />

            <div className="report-actions">

    <button
        className="primary-btn"
        onClick={() => downloadReport("pdf")}
    >
        📄 Export PDF
    </button>

    <button
        className="primary-btn"
        onClick={() => downloadReport("excel")}
    >
        📊 Export Excel
    </button>

    <button
        className="primary-btn"
        onClick={() => downloadReport("csv")}
    >
        📑 Export CSV
    </button>

    <button
        className="primary-btn"
        onClick={() => downloadReport("json")}
    >
        🗂 Export JSON
    </button>

</div>

        </>

    );

}