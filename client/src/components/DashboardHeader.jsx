import "./../style/dashboardHeader.css";

export default function DashboardHeader() {
  const hour = new Date().getHours();

  let greeting = "Good Evening";

  if (hour < 12) greeting = "Good Morning";
  else if (hour < 18) greeting = "Good Afternoon";

  return (
    <div className="dashboard-header">

      <div>
        <h1>{greeting} 👋</h1>

        <p>
          Welcome back! Here's your financial overview.
        </p>
      </div>

    </div>
  );
}