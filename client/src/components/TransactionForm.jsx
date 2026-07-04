import { useState } from "react";
import "./../style/transactionForm.css";

export default function TransactionForm({onSubmit}) {
    const [loading, setLoading] = useState(false);

    const [form, setForm] = useState({

        type: "expense",

        amount: "",

        category: "",

        paymentMethod: "",

        description: "",

        date: new Date().toISOString().split("T")[0],

    });

    const handleChange = (e) => {

        setForm({

            ...form,

            [e.target.name]: e.target.value,

        });

    };

    return (

        <form
    className="transaction-form"
    onSubmit={(e) => {

        e.preventDefault();

        onSubmit(form);

    }}
>

            <div className="form-group">

                <label>Type</label>

                <select
                    name="type"
                    value={form.type}
                    onChange={handleChange}
                >

                    <option value="expense">
                        Expense
                    </option>

                    <option value="income">
                        Income
                    </option>

                </select>

            </div>

            <div className="form-group">

                <label>Amount</label>

                <input
                    type="number"
                    name="amount"
                    placeholder="Enter amount"
                    value={form.amount}
                    onChange={handleChange}
                />

            </div>

            <div className="form-group">

                <label>Category</label>

                <input
                    type="text"
                    name="category"
                    placeholder="Food"
                    value={form.category}
                    onChange={handleChange}
                />

            </div>

            <div className="form-group">

                <label>Payment Method</label>

                <input
                    type="text"
                    name="paymentMethod"
                    placeholder="Cash / UPI"
                    value={form.paymentMethod}
                    onChange={handleChange}
                />

            </div>

            <div className="form-group">

                <label>Description</label>

                <textarea
                    name="description"
                    placeholder="Optional..."
                    value={form.description}
                    onChange={handleChange}
                />

            </div>

            <div className="form-group">

                <label>Date</label>

                <input
                    type="date"
                    name="date"
                    value={form.date}
                    onChange={handleChange}
                />

            </div>

            <button
                className="primary-btn"
                type="submit"
            >
                Save Transaction
            </button>

        </form>

    );

}