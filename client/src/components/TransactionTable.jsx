import "../style/transactionTable.css";

export default function TransactionTable({ transactions,
    onDelete}) {
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

          {transactions.map((transaction) => (

            <tr key={transaction._id}>

              <td>
                {new Date(transaction.date).toLocaleDateString()}
              </td>

              <td>

<span
className={
transaction.type === "income"
? "badge income"
: "badge expense"
}
>

{transaction.type}

</span>

</td>

              <td>{transaction.category}</td>

            <td
            className={
            transaction.type === "income"
            ? "income-text"
            : "expense-text"
            }
            >

            ₹{transaction.amount}

            </td>

              <td>{transaction.paymentMethod}</td>

              <td>{transaction.description}</td>

              <td>

            <button className="action-btn">
                <i className="ti ti-edit"></i>
            </button>

            <button
                  className="delete-btn"
                  onClick={() =>
                    onDelete(transaction._id)
                  }
                >

                  <i className="ti ti-trash"></i>

                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}