import "../style/reportSummary.css";

export default function ReportSummary({ summary }) {

  const cards = [
    {
      title: "Total Income",
      value: `₹${summary.totalIncome.toLocaleString()}`
    },
    {
      title: "Total Expense",
      value: `₹${summary.totalExpense.toLocaleString()}`
    },
    {
      title: "Balance",
      value: `₹${summary.balance.toLocaleString()}`
    },
    {
      title: "Transactions",
      value: summary.totalTransactions
    }
  ];

  return (
    <div className="report-grid">
      {cards.map((card) => (
        <div
          key={card.title}
          className="report-card"
        >
          <h3>{card.title}</h3>
          <h2>{card.value}</h2>
        </div>
      ))}
    </div>
  );
}