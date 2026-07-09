import ReportFilters from "../components/ReportFilters.jsx";
import ReportSummary from "../components/ReportSummary.jsx";

export default function Reports() {
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

            <ReportFilters />

            <ReportSummary />

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