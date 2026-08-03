import { useState } from "react";

import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer
} from "recharts";

import "./barGraph.css";



export default function BarGraph({ transactions = [] }) {


    const [selectedCategory, setSelectedCategory] = useState(null);




    const categoryData = Object.values(

        transactions.reduce((acc, item) => {


            const category = item.category?.trim();


            if (!acc[category]) {

                acc[category] = {

                    category,

                    amount: 0

                };

            }


            acc[category].amount += Number(item.amount);


            return acc;


        }, {})

    );






    const filteredTransactions = transactions.filter(

        item =>

        item.category?.trim() === selectedCategory?.trim()

    );






    const totalAmount = filteredTransactions.reduce(

        (sum, item) =>

        sum + Number(item.amount),

        0

    );







    return (


        <div className="bar-chart-card">





            <h2 className="bar-chart-title">

                Expense Analytics

            </h2>



            <p className="bar-chart-subtitle">

                Click on any category bar to view transactions

            </p>








            {

            categoryData.length === 0 ?



            (

                <div className="bar-empty">

                    No expense data available.

                </div>

            )



            :



            (

            <ResponsiveContainer

                width="100%"

                height={350}

            >



                <BarChart

                    data={categoryData}

                    margin={{

                        top:20,

                        right:20,

                        left:0,

                        bottom:10

                    }}

                >



                    <CartesianGrid

                        strokeDasharray="3 3"

                    />





                    <XAxis

                        dataKey="category"

                    />





                    <YAxis />





                    <Tooltip

                        formatter={(value)=>

                            [`₹${value}`, "Expense"]

                        }

                    />







                    <Bar


                        dataKey="amount"


                        fill="#4F46E5"


                        radius={[10,10,0,0]}


                        cursor="pointer"



                        onClick={(data)=>{


                            setSelectedCategory(

                                data.category

                            );


                        }}



                    />




                </BarChart>



            </ResponsiveContainer>

            )

            }









            {

            selectedCategory && (




            <div className="bar-transaction-section">






                <div className="bar-transaction-header">



                    <div>


                        <h3 className="bar-transaction-title">


                            {selectedCategory}

                            {" "}Transactions


                        </h3>




                        <div className="bar-transaction-info">



                            <span className="bar-count">


                                {filteredTransactions.length}

                                {" "}transactions


                            </span>





                            <span className="bar-total">


                                Total:

                                {" "}

                                ₹{totalAmount}


                            </span>




                        </div>


                    </div>







                    <button


                        className="bar-clear-btn"


                        onClick={()=>setSelectedCategory(null)}



                    >

                        Clear


                    </button>




                </div>









                {


                filteredTransactions.length === 0 ?



                (

                    <div className="bar-empty">

                        No transactions found.

                    </div>


                )



                :



                (


                <div className="bar-transaction-list">






                {

                filteredTransactions.map((item)=>(



                    <div


                        key={item._id}


                        className="bar-transaction-card"



                    >







                        <div className="bar-transaction-left">





                            <div className="bar-icon">


                                ₹


                            </div>






                            <div>




                                <h4 className="bar-title">


                                    {item.title}


                                </h4>





                                <div className="bar-meta">



                                    <span className="bar-category">


                                        {item.category}


                                    </span>





                                    <span className="bar-date">


                                        {

                                        new Date(item.date)

                                        .toLocaleDateString()

                                        }


                                    </span>



                                </div>




                            </div>





                        </div>









                        <div className="bar-amount-box">



                            <p className="bar-amount">


                                - ₹{item.amount}


                            </p>





                            <span className="bar-type">


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