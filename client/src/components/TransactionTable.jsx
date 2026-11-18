import "../style/transactionTable.css";

export default function TransactionTable({
  transactions = [],
  onDelete,
  onEdit,
}) {
  return (
    <div className="table-container">
      <table className="transaction-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Type</th>
            <th>Category</th>
            <th>Amount</th>
            <th>Payment</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {transactions.length === 0 ? (
            <tr>
              <td
                colSpan="7"
                style={{
                  textAlign: "center",
                  padding: "2.5rem 1rem",
                  color: "#64748b",
                  fontSize: "1rem",
                }}
              >
                No transactions found. Click <strong>+ Add Transaction</strong> to record a new entry!
              </td>
            </tr>
          ) : (
            transactions.map((transaction) => {
              const isIncome =
                transaction.type?.toLowerCase() === "income";
              const formattedDate = transaction.date
                ? new Date(transaction.date).toLocaleDateString()
                : "Recent";

              return (
                <tr key={transaction._id}>
                  <td>{formattedDate}</td>

                  <td>
                    <span
                      className={
                        isIncome ? "badge income" : "badge expense"
                      }
                    >
                      {transaction.type || "expense"}
                    </span>
                  </td>

                  <td>{transaction.category || "General"}</td>

                  <td className={isIncome ? "income-text" : "expense-text"}>
                    {isIncome ? "+" : "-"} ₹{Number(transaction.amount || 0).toLocaleString()}
                  </td>

                  <td>{transaction.paymentMethod || "Cash"}</td>

                  <td>{transaction.description || "-"}</td>

                  <td>
                    <button
                      className="edit-btn"
                      onClick={() => onEdit(transaction)}
                      title="Edit Transaction"
                    >
                      <i className="ti ti-edit"></i>
                    </button>

                    <button
                      className="delete-btn"
                      onClick={() => onDelete(transaction._id)}
                      title="Delete Transaction"
                    >
                      <i className="ti ti-trash"></i>
                    </button>
                  </td>
                </tr>
              );
            })
          )}
        </tbody>
      </table>
    </div>
  );
}