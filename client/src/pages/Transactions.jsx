import { useEffect, useState } from "react";
import TransactionTable from "../components/TransactionTable.jsx";
import AddTransactionModal from "../components/AddTransactionModal.jsx";
import TransactionForm from "../components/TransactionForm.jsx";

export default function Transactions() {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    async function fetchTransactions() {
      try {
        const response = await fetch(
          "http://localhost:5000/api/transactions",
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
          }
        );

        const data = await response.json();

        setTransactions(data.transactions);

      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    }

    fetchTransactions();
  }, []);

  // Delete Transaction
  const handleDelete = async (id) => {

    const confirmDelete = window.confirm(
      "Are you sure you want to delete this transaction?"
    );

    if (!confirmDelete) return;

    try {

      const response = await fetch(
        `http://localhost:5000/api/transactions/${id}`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );

      const data = await response.json();

      if (data.success) {

        setTransactions(
          transactions.filter(
            (transaction) => transaction._id !== id
          )
        );

      } else {

        alert(data.message);

      }

    } catch (error) {

      console.log(error);
      alert("Failed to delete transaction.");

    }

  };
// add transaction
  const handleAddTransaction = async (formData) => {

    try {

        const response = await fetch(
            "http://localhost:5000/api/transactions",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",

                    Authorization:
                        `Bearer ${localStorage.getItem("token")}`,
                },

                body: JSON.stringify(formData),

            }
        );

        const data = await response.json();

        if (data.success) {

            setTransactions([
                data.transaction,
                ...transactions,
            ]);

            setShowModal(false);

        } else {

            alert(data.message);

        }

    } catch (error) {

        console.log(error);

    }

};

  if (loading) return <h2>Loading...</h2>;

  return (
    <>
      <div className="page-header">

        <h1>Transactions</h1>

        <button
    className="primary-btn"
    onClick={() => setShowModal(true)}
>
          + Add Transaction
        </button>

      </div>

      <TransactionTable
        transactions={transactions}
        onDelete={handleDelete}
      />
      {
    showModal && (

        <AddTransactionModal

            onClose={() => setShowModal(false)}

        >

            <TransactionForm onSubmit={handleAddTransaction}/>

        </AddTransactionModal>

    )
}
    </>
  );
}