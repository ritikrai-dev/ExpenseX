import { useEffect, useState } from "react";
import { useLocation, Link } from "react-router-dom";
import { getUser, isDemo } from "./data/dataService";
import "../style/navbar.css";

export default function Navbar({ sidebarOpen, setSidebarOpen }) {
  const [user, setUser] = useState(null);
  const location = useLocation();
  const demoActive = isDemo();

  useEffect(() => {
    async function fetchUserData() {
      try {
        const u = await getUser();
        if (u) {
          setUser(u);
        }
      } catch (error) {
        console.error("User Fetch Error:", error);
      }
    }

    fetchUserData();
  }, [location.pathname]);

  const pageDetails = {
    "/dashboard": {
      title: "Dashboard",
      icon: "ti-home",
    },
    "/transactions": {
      title: "Transactions",
      icon: "ti-receipt",
    },
    "/analytics": {
      title: "Analytics",
      icon: "ti-chart-bar",
    },
    "/ai": {
      title: "AI Insights",
      icon: "ti-sparkles",
    },
    "/reports": {
      title: "Reports",
      icon: "ti-file-text",
    },
    "/settings": {
      title: "Settings",
      icon: "ti-settings",
    },
  };

  const currentPage = pageDetails[location.pathname] || {
    title: "ExpenseX",
    icon: "ti-layout-dashboard",
  };

  const userName =
    user?.name ||
    user?.username ||
    user?.fullName ||
    (demoActive ? "Guest User" : "User");

  return (
    <header className="navbar">
      <div className="navbar-left">
        <button
          className="menu-toggle"
          onClick={() => setSidebarOpen((prev) => !prev)}
          aria-label="Toggle navigation menu"
        >
          <i className="ti ti-menu-2"></i>
        </button>

        <h2>
          <i className={`ti ${currentPage.icon}`}></i>
          {currentPage.title}
        </h2>
      </div>

      <div className="navbar-right">
        {demoActive && (
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: "0.5rem",
              background: "#e0e7ff",
              color: "#3730a3",
              padding: "4px 10px",
              borderRadius: "20px",
              fontSize: "0.82rem",
              fontWeight: "600",
            }}
          >
            <span>👤 Guest Mode</span>
            <Link
              to="/auth"
              style={{
                background: "#4f46e5",
                color: "#ffffff",
                padding: "2px 8px",
                borderRadius: "12px",
                textDecoration: "none",
                fontSize: "0.75rem",
              }}
            >
              Log In
            </Link>
          </div>
        )}

        <button className="icon-btn" aria-label="Notifications">
          <i className="ti ti-bell"></i>
        </button>

        <div className="profile">
          <img
            src={`https://ui-avatars.com/api/?name=${encodeURIComponent(
              userName
            )}&background=4f46e5&color=fff`}
            alt="avatar"
          />
          <span>{userName}</span>
        </div>
      </div>
    </header>
  );
}