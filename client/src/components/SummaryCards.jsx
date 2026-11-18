import "./../style/summaryCards.css";

export default function SummaryCards({ dashboard }) {

  const cards = [

    {
        title: "Balance",
        amount: `₹${(dashboard?.balance ?? 0).toLocaleString()}`,
        icon: "ti ti-wallet",
    },

    {
        title: "Income",
        amount: `₹${(dashboard?.totalIncome ?? 0).toLocaleString()}`,
        icon: "ti ti-arrow-up",
    },

    {
        title: "Expense",
        amount: `₹${(dashboard?.totalExpense ?? 0).toLocaleString()}`,
        icon: "ti ti-arrow-down",
    },

    {
        title: "Transactions",
        amount: dashboard?.totalTransactions ?? 0,
        icon: "ti ti-receipt",
    },

];
  return (
    <div className="summary-grid">

      {cards.map((card) => (

        <div
          className="summary-card"
          key={card.title}
        >

          <div className="summary-icon">

            <i className={card.icon}></i>

          </div>

          <div>

            <p>{card.title}</p>

            <h2>{card.amount}</h2>

          </div>

        </div>

      ))}

    </div>
  );
}