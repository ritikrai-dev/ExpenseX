import { useState } from "react";

import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    Legend,
    ResponsiveContainer
} from "recharts";

import "../style/expenseCategoryChart.css";


const COLORS = [
    "#4F46E5",
    "#22C55E",
    "#F59E0B",
    "#EF4444",
    "#06B6D4",
    "#8B5CF6"
];



export default function ExpenseCategoryChart({

    data,

    transactions = []

}) {


    const [selectedCategory, setSelectedCategory] = useState(null);



    const filteredTransactions = transactions.filter(

        (item) =>

            item.category?.trim() === selectedCategory?.trim()

    );



    const totalExpense = filteredTransactions.reduce(

        (sum, item) => sum + Number(item.amount),

        0

    );





    return (

        <div className="expense-chart-card">



            <h2 className="expense-chart-title">

                Expense Categories

            </h2>





            {
                data.length === 0 ?


                (

                    <div className="empty-box">

                        No expense data available.

                    </div>

                )


                :


                (

                <ResponsiveContainer

                    width="100%"

                    height={350}

                >


                    <PieChart>


                        <Pie

                            data={data}

                            dataKey="value"

                            nameKey="name"

                            cx="50%"

                            cy="50%"

                            outerRadius={110}

                            innerRadius={55}

                            cursor="pointer"

                            onClick={(item)=>{

                                setSelectedCategory(item.name);

                            }}

                        >



                            {

                            data.map((entry,index)=>(


                                <Cell

                                    key={index}

                                    fill={
                                        COLORS[index % COLORS.length]
                                    }

                                />


                            ))

                            }



                        </Pie>



                        <Tooltip />



                        <Legend />



                    </PieChart>



                </ResponsiveContainer>

                )

            }








            {

            selectedCategory && (


            <div className="transaction-section">





                <div className="transaction-header">



                    <div>


                        <h3 className="transaction-title">

                            {selectedCategory} Transactions

                        </h3>



                        <p className="transaction-count">

                            {filteredTransactions.length}

                            {" "}transactions found

                        </p>



                        <p className="total-expense">

                            Total Spent:
                            {" "}
                            ₹{totalExpense}


                        </p>



                    </div>





                    <button

                        className="clear-btn"

                        onClick={()=>setSelectedCategory(null)}

                    >

                        Clear

                    </button>



                </div>







                {

                filteredTransactions.length === 0 ?


                (

                    <div className="empty-box">

                        No transactions found.

                    </div>

                )


                :



                (

                <div className="transaction-list">



                {

                filteredTransactions.map((item)=>(



                    <div

                        className="transaction-card"

                        key={item._id}

                    >




                        <div className="transaction-left">



                            <div className="transaction-icon">

                                ₹

                            </div>





                            <div>



                                <h4 className="transaction-name">

                                    {item.title}

                                </h4>





                                <div className="transaction-meta">



                                    <span className="category-badge">

                                        {item.category}

                                    </span>




                                    <span className="date-text">

                                        {

                                        new Date(item.date)

                                        .toLocaleDateString()

                                        }

                                    </span>



                                </div>



                            </div>



                        </div>







                        <div className="transaction-right">



                            <p className="transaction-amount">

                                - ₹{item.amount}

                            </p>



                            <span className="expense-badge">

                                Expense

                            </span>



                        </div>





                    </div>



                ))

                }



                </div>

                )

                }







            </div>


            )

            }





        </div>

    );

}