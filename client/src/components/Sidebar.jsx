import { NavLink } from "react-router-dom";
import "../style/sidebar.css";
export default function Sidebar() {
  return (
    <aside className="sidebar">

      <div className="sidebar-logo">
        <img
    src="/logo1.png"
    alt="ExpenseX AI Logo"
    className="logo-img"
  />
        <h2>ExpenseX</h2>
      </div>

      <nav className="sidebar-menu">

        <NavLink to="/dashboard" className="menu-item">
          <i className="ti ti-home"></i>
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/transactions" className="menu-item">
          <i className="ti ti-receipt"></i>
          <span>Transactions</span>
        </NavLink>

        <NavLink to="/analytics" className="menu-item">
          <i className="ti ti-chart-bar"></i>
          <span>Analytics</span>
        </NavLink>

        <NavLink to="/ai" className="menu-item">
          <i className="ti ti-sparkles"></i>
          <span>AI Insights</span>
        </NavLink>

        <NavLink to="/reports" className="menu-item">
          <i className="ti ti-file-text"></i>
          <span>Reports</span>
        </NavLink>

        <NavLink to="/settings" className="menu-item">
          <i className="ti ti-settings"></i>
          <span>Settings</span>
        </NavLink>

      </nav>

      <button className="logout-btn">
        <i className="ti ti-logout"></i>
        Logout
      </button>

    </aside>
  );
}