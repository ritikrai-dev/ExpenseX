import { useEffect, useState } from "react";
import TransactionTable from "../components/TransactionTable";
import AddTransactionModal from "../components/AddTransactionModal";
import TransactionForm from "../components/TransactionForm";
import SearchBar from "../components/SearchBar";
import TransactionFilter from "../components/TransactionFilter";
import Pagination from "../components/Pagination";
import { toast } from "react-toastify";

import {
  getTransactions,
  addTransaction,
  updateTransaction,
  deleteTransaction,
} from "../components/data/dataService";

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
    loadTransactions();
  }, []);

  async function loadTransactions() {
    try {
      setLoading(true);

      const data = await getTransactions();

      // Backend returns:
      // { transactions, totalPages }

      // Demo returns:
      // [ ...]

      if (Array.isArray(data)) {
        setTransactions(data);
        setTotalPages(1);
      } else {
        setTransactions(data.transactions || []);
        setTotalPages(data.totalPages || 1);
      }
    } catch (err) {
      console.log(err);
      toast.error("Failed to load transactions");
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(id) {
    const confirmDelete = window.confirm(
      "Delete this transaction?"
    );

    if (!confirmDelete) return;

    try {
      await deleteTransaction(id);

      setTransactions((prev) =>
        prev.filter((t) => t._id !== id)
      );

      toast.success("Transaction deleted");
    } catch (err) {
      console.log(err);
      toast.error("Delete failed");
    }
  }

  async function handleAddTransaction(formData) {
    try {
      const transaction = await addTransaction(formData);

      setTransactions((prev) => [
        transaction,
        ...prev,
      ]);

      setShowModal(false);

      toast.success("Transaction added");
    } catch (err) {
      console.log(err);
      toast.error("Failed to add transaction");
    }
  }

  function handleEdit(transaction) {
    setSelectedTransaction(transaction);
    setShowModal(true);
  }

  async function handleUpdateTransaction(formData) {
    try {
      const updated = await updateTransaction(
        selectedTransaction._id,
        formData
      );

      setTransactions((prev) =>
        prev.map((t) =>
          t._id === updated._id ? updated : t
        )
      );

      setSelectedTransaction(null);
      setShowModal(false);

      toast.success("Transaction updated");
    } catch (err) {
      console.log(err);
      toast.error("Update failed");
    }
  }

  const filteredTransactions = transactions.filter((transaction) => {
    const category =
      transaction.category?.toLowerCase() || "";

    const description =
      transaction.description?.toLowerCase() ||
      transaction.note?.toLowerCase() ||
      "";

    const paymentMethod =
      transaction.paymentMethod?.toLowerCase() || "";

    const query = search.toLowerCase();

    const matchesSearch =
      category.includes(query) ||
      description.includes(query) ||
      paymentMethod.includes(query);

    const matchesFilter =
      filter === "all" ||
      transaction.type?.toLowerCase() === filter.toLowerCase();

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
            onClick={() => {
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

      {showModal && (
        <AddTransactionModal
          onClose={() => {
            setShowModal(false);
            setSelectedTransaction(null);
          }}
        >
          <TransactionForm
            transaction={selectedTransaction}
            onSubmit={
              selectedTransaction
                ? handleUpdateTransaction
                : handleAddTransaction
            }
          />
        </AddTransactionModal>
      )}
    </>
  );
}