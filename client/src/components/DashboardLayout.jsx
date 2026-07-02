import Sidebar from "./Sidebar";
import Navbar from "./Navbar";
import "../style/dashboard.css";

export default function DashboardLayout({ children }) {
  return (
    <div className="dashboard">

      <Sidebar />

      <div className="dashboard-main">

        <Navbar />

        <div className="dashboard-content">
          {children}
        </div>

      </div>

    </div>
  );
}