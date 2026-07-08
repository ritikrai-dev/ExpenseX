import "../style/aiInsight.css";

export default function AIInsightCard({ insights }) {

    if (!insights) return null;

    return (

        <div className="ai-grid">

            <div className="ai-card">

                <h3>💚 Financial Health</h3>

                <h2>{insights.financialHealth}</h2>

                <p>Score : {insights.score}/100</p>

            </div>

            <div className="ai-card">

                <h3>📊 Spending Analysis</h3>

                <p>{insights.spendingAnalysis}</p>

            </div>

            <div className="ai-card">

                <h3>💰 Savings Recommendation</h3>

                <p>{insights.savingsRecommendation}</p>

            </div>

            <div className="ai-card">

                <h3>🏆 Highest Expense</h3>

                <p>{insights.highestExpenseCategory}</p>

                <h2>₹{insights.highestExpenseAmount}</h2>

            </div>

            <div className="ai-card">

                <h3>⚠ Smart Alerts</h3>

                <ul>

                    {insights.smartAlerts.map((alert,index)=>(

                        <li key={index}>{alert}</li>

                    ))}

                </ul>

            </div>

            <div className="ai-card">

                <h3>💡 Personalized Tips</h3>

                <ul>

                    {insights.personalizedTips.map((tip,index)=>(

                        <li key={index}>{tip}</li>

                    ))}

                </ul>

            </div>

            <div className="ai-card">

                <h3>🎯 Next Month Goal</h3>

                <p>{insights.nextMonthGoal}</p>

            </div>

        </div>

    );

}