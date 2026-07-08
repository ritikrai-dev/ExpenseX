import { useEffect, useState } from "react";
import AIInsightCard from "../components/AIInsightCard";

export default function AIInsights() {

    const [insights, setInsights] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetchInsights();

    }, []);

    const fetchInsights = async () => {

        try {

            const response = await fetch(

                "http://localhost:5000/api/ai/insights",

                {

                    headers: {

                        Authorization: `Bearer ${localStorage.getItem("token")}`

                    }

                }

            );

            const data = await response.json();

            setInsights(data.insights);

        }

        catch(error){

            console.log(error);

        }

        finally{

            setLoading(false);

        }

    };

    if(loading){

        return <h2>Generating AI Insights...</h2>;

    }

    return(

        <>

            <div className="page-header">

                <h1>🤖 AI Financial Insights</h1>

                <button

                    className="primary-btn"

                    onClick={fetchInsights}

                >

                    Refresh

                </button>

            </div>

            <AIInsightCard insights={insights}/>

        </>

    );

}