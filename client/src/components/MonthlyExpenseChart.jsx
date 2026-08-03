import {

LineChart,
Line,
XAxis,
YAxis,
Tooltip,
ResponsiveContainer,
CartesianGrid

} from "recharts";

import "../style/monthlyExpenseChart.css";


export default function MonthlyExpenseChart({data}){


    if (!data || data.length === 0) {

        return (

            <div className="monthly-chart-card">

                <h2 className="monthly-chart-title">
                    Monthly Expense
                </h2>

                <p className="monthly-empty-text">
                    No monthly expense data available yet.
                </p>

            </div>

        );

    }


return(

<div className="monthly-chart-card">


<h2 className="monthly-chart-title">
    Monthly Expense
</h2>



<ResponsiveContainer

width="100%"

height={350}

>


<LineChart data={data}>


<CartesianGrid 
    strokeDasharray="3 3"
/>



<XAxis

    dataKey="month"

    tick={{ fontSize: 12 }}

/>



<YAxis

    tick={{ fontSize: 12 }}

/>



<Tooltip

    contentStyle={{

        borderRadius:"10px"

    }}

/>



<Line

    type="monotone"

    dataKey="amount"

    stroke="#4F46E5"

    strokeWidth={3}

    dot={{ r:4 }}

    activeDot={{ r:7 }}

/>



</LineChart>


</ResponsiveContainer>



</div>

);

}