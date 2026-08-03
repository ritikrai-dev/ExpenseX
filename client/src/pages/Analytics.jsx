import { useEffect, useState } from "react";

import ExpenseCategoryChart from "../components/ExpenseCategoryChart.jsx";
import MonthlyExpenseChart from "../components/MonthlyExpenseChart.jsx";

import "../style/analytics.css";



export default function Analytics() {


    const [categoryData, setCategoryData] = useState([]);

    const [monthlyData, setMonthlyData] = useState([]);

    const [transactions, setTransactions] = useState([]);





    useEffect(() => {


        fetchCategory();

        fetchMonthly();

        fetchTransactions();


    }, []);







    async function fetchCategory() {


        try {


            const response = await fetch(


                `${import.meta.env.VITE_API_URL}/api/analytics/category`,


                {

                    headers: {

                        Authorization:

                        `Bearer ${localStorage.getItem("token")}`

                    }

                }


            );



            const data = await response.json();





            const formatted = Object.entries(

                data.categoryData || {}

            ).map(([name, value]) => ({


                name,

                value


            }));





            setCategoryData(formatted);



        } catch(error) {


            console.error(

                "Category Analytics Error:",

                error

            );


        }


    }









    async function fetchMonthly() {


        try {


            const response = await fetch(


                `${import.meta.env.VITE_API_URL}/api/analytics/monthly-expense`,


                {

                    headers: {


                        Authorization:

                        `Bearer ${localStorage.getItem("token")}`


                    }


                }


            );





            const data = await response.json();





            setMonthlyData(

                data.monthlyExpense || []

            );



        } catch(error) {


            console.error(

                "Monthly Analytics Error:",

                error

            );


        }


    }









    async function fetchTransactions() {


        try {


            const response = await fetch(


                `${import.meta.env.VITE_API_URL}/api/transactions`,


                {

                    headers: {


                        Authorization:

                        `Bearer ${localStorage.getItem("token")}`


                    }


                }


            );





            const data = await response.json();





            setTransactions(

                data.transactions || data || []

            );



        } catch(error) {


            console.error(

                "Transaction Error:",

                error

            );


        }


    }









    return (



        <div className="analytics-container">





            <div className="analytics-grid">





                <div className="analytics-card-wrapper">


                    <ExpenseCategoryChart


                        data={categoryData}


                        transactions={transactions}


                    />


                </div>







                <div className="analytics-card-wrapper">


                    <MonthlyExpenseChart


                        data={monthlyData}


                    />


                </div>






            </div>





        </div>


    );

}