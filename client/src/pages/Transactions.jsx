import { useEffect, useState } from "react";
import TransactionTable from "../components/TransactionTable.jsx";
import AddTransactionModal from "../components/AddTransactionModal.jsx";
import TransactionForm from "../components/TransactionForm.jsx";
import SearchBar from "../components/SearchBar.jsx";
import TransactionFilter from "../components/TransactionFilter.jsx";
import Pagination from "../components/Pagination";


export default function Transactions() {
  const [transactions, setTransactions] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [selectedTransaction, setSelectedTransaction] = useState(null);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("all");

  useEffect(() => {
    async function fetchTransactions() {
      try {
        const response = await fetch(
          `${import.meta.env.VITE_API_URL}/api/transactions?page=${page}&limit=10`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
          }
        );

        const data = await response.json();

        setTransactions(data.transactions);
        setTotalPages(data.totalPages);

      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    }

    fetchTransactions();
  }, [page]);

  // Delete Transaction
  const handleDelete = async (id) => {

    const confirmDelete = window.confirm(
      "Are you sure you want to delete this transaction?"
    );

    if (!confirmDelete) return;

    try {

      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/transactions/${id}`,
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
            `${import.meta.env.VITE_API_URL}/api/transactions`,
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

const handleEdit = (transaction) => {

    setSelectedTransaction(transaction);

    setShowModal(true);

};

const handleUpdateTransaction = async (formData) => {

    try {

        const response = await fetch(

            `${import.meta.env.VITE_API_URL}/api/transactions/${selectedTransaction._id}`,

            {

                method: "PUT",

                headers: {

                    "Content-Type": "application/json",

                    Authorization:
                        `Bearer ${localStorage.getItem("token")}`

                },

                body: JSON.stringify(formData)

            }

        );

        const data = await response.json();

        if (data.success) {

            setTransactions(

                transactions.map((transaction) =>

                    transaction._id === data.transaction._id

                        ? data.transaction

                        : transaction

                )

            );

            setSelectedTransaction(null);

            setShowModal(false);

        }

        else {

            alert(data.message);

        }

    }

    catch (error) {

        console.log(error);

    }

};

const filteredTransactions = transactions.filter((transaction) => {

    const matchesSearch =

        transaction.category
            .toLowerCase()
            .includes(search.toLowerCase())

        ||

        transaction.description
            .toLowerCase()
            .includes(search.toLowerCase())

        ||

        transaction.paymentMethod
            .toLowerCase()
            .includes(search.toLowerCase());

    const matchesFilter =

        filter === "all"

        ||

        transaction.type === filter;

    return matchesSearch && matchesFilter;

});

  if (loading) return <h2>Loading...</h2>;

  return (
    <>
      <div className="page-header">

        <h1>Transactions</h1>
<div className="page-actions">

    <SearchBar
        search={search}
        setSearch={setSearch}
    />

    <button
        className="primary-btn"
        onClick={()=>{
            setSelectedTransaction(null);
            setShowModal(true);
        }}
    >
        + Add Transaction
    </button>

    <TransactionFilter
    filter={filter}
    setFilter={setFilter}
/>

</div>
      </div>

      <TransactionTable
        transactions={filteredTransactions}
        onDelete={handleDelete}
        onEdit={handleEdit}
      />
      <Pagination

page={page}

totalPages={totalPages}

setPage={setPage}

/>
      {
    showModal && (

        <AddTransactionModal

            onClose={() => setShowModal(false)}

        >

            <TransactionForm

    transaction={selectedTransaction}

    onSubmit={

        selectedTransaction

        ?

        handleUpdateTransaction

        :

        handleAddTransaction

    }

/>

        </AddTransactionModal>

    )
}
    </>
  );
}