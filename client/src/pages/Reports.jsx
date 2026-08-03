import ReportSummary from "../components/ReportSummary.jsx";
import "../style/report.css";
import { useEffect, useState } from "react";


export default function Reports() {


    const [summary, setSummary] = useState({

        totalIncome: 0,

        totalExpense: 0,

        balance: 0,

        totalTransactions: 0

    });



    const [fromDate, setFromDate] = useState("");

    const [toDate, setToDate] = useState("");





    async function fetchSummary() {


        try {


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



            setSummary({

                totalIncome: data.dashboard.totalIncome,

                totalExpense: data.dashboard.totalExpense,

                balance: data.dashboard.balance,

                totalTransactions: data.dashboard.totalTransactions

            });



        } catch(error) {


            console.log(error);


        }


    }






    useEffect(() => {


        fetchSummary();


    }, []);









    const downloadReport = async(type, filterDate=false) => {


        try {


            let url =

            `${import.meta.env.VITE_API_URL}/api/reports/${type}`;





            if(filterDate && fromDate && toDate) {


                url +=

                `?fromDate=${fromDate}&toDate=${toDate}`;


            }





            const response = await fetch(

                url,

                {

                    headers: {

                        Authorization:

                        `Bearer ${localStorage.getItem("token")}`

                    }

                }

            );





            if(!response.ok) {


                throw new Error(
                    "Download failed"
                );


            }





            const blob = await response.blob();




            const fileUrl =

            window.URL.createObjectURL(blob);





            const link = document.createElement("a");



            link.href = fileUrl;



            link.download =

            `expense-report.${
                
                type === "excel"

                ? 

                "xlsx"

                :

                "pdf"

            }`;





            document.body.appendChild(link);



            link.click();



            link.remove();



            window.URL.revokeObjectURL(fileUrl);



        } catch(error) {


            console.log(error);


        }


    };








    return (

        <>


            <h1 className="page-title">

                Reports

            </h1>





            <ReportSummary

                summary={summary}

            />









            {/* Complete Report Export */}



            <div className="export-section">


                <h2 className="export-title">

                    Export Financial Reports

                </h2>



                <p className="export-subtitle">

                    Download your complete expense history.

                </p>






                <div className="report-actions">


                    <button

                        className="primary-btn"

                        onClick={() =>

                            downloadReport("pdf")

                        }

                    >

                        📄 Export PDF


                    </button>







                    <button

                        className="primary-btn"

                        onClick={() =>

                            downloadReport("excel")

                        }

                    >

                        📊 Export Excel


                    </button>




                </div>



            </div>









            {/* Date Based Report */}





            <div className="export-section date-report-section">



                <h2 className="export-title">

                    Download Report By Date

                </h2>





                <p className="export-subtitle">

                    Select date range and download filtered transactions.

                </p>









                <div className="date-filter">





                    <div>


                        <label>

                            From Date

                        </label>



                        <input

                            type="date"

                            value={fromDate}

                            onChange={(e)=>

                                setFromDate(
                                    e.target.value
                                )

                            }

                        />


                    </div>








                    <div>


                        <label>

                            To Date

                        </label>




                        <input

                            type="date"

                            value={toDate}

                            onChange={(e)=>

                                setToDate(
                                    e.target.value
                                )

                            }

                        />


                    </div>





                </div>









                <div className="report-actions">





                    <button

                        className="primary-btn"

                        onClick={() =>

                            downloadReport(
                                "pdf",
                                true
                            )

                        }

                    >

                        📄 Download PDF


                    </button>








                    <button

                        className="primary-btn"

                        onClick={() =>

                            downloadReport(
                                "excel",
                                true
                            )

                        }

                    >

                        📊 Download Excel


                    </button>







                </div>





            </div>






        </>

    );

}