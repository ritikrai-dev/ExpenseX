import "../style/recentTransactions.css";
import { Link } from "react-router-dom";

export default function RecentTransactions({ transactions }) {
  return (
    <div className="recent-transactions">

      <div className="section-header">
        <h2>Recent Transactions</h2>
        <Link
    to="/transactions"
    className="view-all-btn"
>
    View All
</Link>
      </div>

      {
        transactions.map((transaction) => (

          <div
            className="transaction-card"
            key={transaction._id}
          >

            <div className="transaction-left">

              <div
                className={`transaction-icon ${
                  transaction.type === "income"
                    ? "income"
                    : "expense"
                }`}
              >

                <i
                  className={
                    transaction.type === "income"
                      ? "ti ti-arrow-up"
                      : "ti ti-arrow-down"
                  }
                ></i>

              </div>

              <div>

                <h4>{transaction.category}</h4>

                <span>{transaction.paymentMethod}</span>

              </div>

            </div>

            <div className="transaction-right">

              <h3
                className={
                  transaction.type === "income"
                    ? "income-text"
                    : "expense-text"
                }
              >
                {transaction.type === "income" ? "+" : "-"}₹
                {transaction.amount}
              </h3>

              <small>
                {new Date(transaction.date).toLocaleDateString()}
              </small>

            </div>

          </div>

        ))
      }

    </div>
  );
}