import { NavLink, useNavigate } from "react-router-dom";
import { isDemo, disableDemoMode } from "./data/demoService";
import "../style/sidebar.css";

export default function Sidebar({ sidebarOpen, setSidebarOpen }) {
  const navigate = useNavigate();
  const demoActive = isDemo();

  const handleLogout = () => {
    const confirmLogout = window.confirm(
      demoActive
        ? "Exit Guest Mode and return to home?"
        : "Are you sure you want to logout?"
    );

    if (!confirmLogout) return;

    localStorage.removeItem("token");
    localStorage.removeItem("user");
    disableDemoMode();
    navigate("/", { replace: true });
  };

  return (
    <aside className={`sidebar ${sidebarOpen ? "open" : ""}`}>
      <div className="sidebar-logo">
        <img
          src="/logo1.png"
          alt="ExpenseX AI Logo"
          className="logo-img"
        />
        <h2>ExpenseX</h2>
      </div>

      <nav className="sidebar-menu">
        <NavLink
          to="/dashboard"
          className="menu-item"
          onClick={() => setSidebarOpen(false)}
        >
          <i className="ti ti-home"></i>
          <span>Dashboard</span>
        </NavLink>

        <NavLink
          to="/transactions"
          className="menu-item"
          onClick={() => setSidebarOpen(false)}
        >
          <i className="ti ti-receipt"></i>
          <span>Transactions</span>
        </NavLink>

        <NavLink
          to="/analytics"
          className="menu-item"
          onClick={() => setSidebarOpen(false)}
        >
          <i className="ti ti-chart-bar"></i>
          <span>Analytics</span>
        </NavLink>

        <NavLink
          to="/ai"
          className="menu-item"
          onClick={() => setSidebarOpen(false)}
        >
          <i className="ti ti-sparkles"></i>
          <span>AI Insights</span>
        </NavLink>

        <NavLink
          to="/reports"
          className="menu-item"
          onClick={() => setSidebarOpen(false)}
        >
          <i className="ti ti-file-text"></i>
          <span>Reports</span>
        </NavLink>

        <NavLink
          to="/settings"
          className="menu-item"
          onClick={() => setSidebarOpen(false)}
        >
          <i className="ti ti-settings"></i>
          <span>Settings</span>
        </NavLink>
      </nav>

      {demoActive && (
        <div
          style={{
            margin: "0.5rem 1rem",
            padding: "0.75rem",
            background: "rgba(99, 102, 241, 0.08)",
            border: "1px solid rgba(99, 102, 241, 0.2)",
            borderRadius: "8px",
            textAlign: "center",
          }}
        >
          <p
            style={{
              fontSize: "0.8rem",
              color: "#4f46e5",
              fontWeight: "600",
              margin: 0,
            }}
          >
            👤 Guest Mode Active
          </p>
          <NavLink
            to="/auth"
            style={{
              display: "inline-block",
              marginTop: "4px",
              fontSize: "0.75rem",
              color: "#3730a3",
              textDecoration: "underline",
              fontWeight: 500,
            }}
            onClick={() => setSidebarOpen(false)}
          >
            Create Permanent Account →
          </NavLink>
        </div>
      )}

      <button className="logout-btn" onClick={handleLogout}>
        <i className="ti ti-logout"></i>
        {demoActive ? "Exit Guest Mode" : "Logout"}
      </button>
    </aside>
  );
}