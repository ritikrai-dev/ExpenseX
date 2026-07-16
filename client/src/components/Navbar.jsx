import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "../style/navbar.css";

export default function Navbar({ sidebarOpen,
  setSidebarOpen, }) {

  const [user, setUser] = useState(null);
  const location = useLocation();
  
  useEffect(() => {
    
    async function fetchUser() {
      const isDemo = localStorage.getItem("demoMode") === "true";
      if (isDemo) {
    const demoUser = JSON.parse(localStorage.getItem("demoUser"));

    setUser(demoUser);

    return;
}

      try {

        const response = await fetch(
          `${import.meta.env.VITE_API_URL}/api/users/profile`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
          }
        );

        const data = await response.json();

        if (data.success) {
          setUser(data.user);
        }

      } catch (error) {
        console.log(error);
      }

    }

    fetchUser();

  }, []);
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

const currentPage =
  pageDetails[location.pathname] || {
    title: "ExpenseX",
    icon: "ti-layout-dashboard",
  };


  return (
    <header className="navbar">

      <div className="navbar-left">

  <button
    className="menu-toggle"
    onClick={() => setSidebarOpen(prev => !prev)}
  >
    <i className="ti ti-menu-2"></i>
  </button>
        <h2>
    <i className={`ti ${currentPage.icon}`}></i>
    {currentPage.title}
  </h2>
      </div>

      <div className="navbar-right">

        <button className="icon-btn">
          <i className="ti ti-bell"></i>
        </button>

        <div className="profile">

          <img
            src={`https://ui-avatars.com/api/?name=${encodeURIComponent(user?.name || "User")}`}
            alt="avatar"
          />

          <span>{user?.name || "Loading..."}</span>

        </div>

      </div>

    </header>
  );
}