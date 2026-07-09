import { useEffect, useState } from "react";
import ExpenseCategoryChart from "../components/ExpenseCategoryChart.jsx";
import MonthlyExpenseChart from "../components/MonthlyExpenseChart.jsx";

export default function Analytics() {

    const [categoryData, setCategoryData] = useState([]);

    const [monthlyData, setMonthlyData] = useState([]);

    useEffect(() => {

        fetchCategory();

        fetchMonthly();

    }, []);

    async function fetchCategory() {

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

        const formatted = Object.entries(data.categoryData).map(

            ([name, value]) => ({

                name,

                value,

            })

        );

        setCategoryData(formatted);

    }

    async function fetchMonthly() {

        const response = await fetch(

            "http://localhost:5000/api/analytics/monthly-expense",

            {

                headers: {

                    Authorization:
                        `Bearer ${localStorage.getItem("token")}`

                }

            }

        );

        const data = await response.json();

        setMonthlyData(data.monthlyExpense);

    }

    return (

        <>

            <ExpenseCategoryChart
                data={categoryData}
            />

            <MonthlyExpenseChart
                data={monthlyData}
            />

        </>

    );

}