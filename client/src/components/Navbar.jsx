import { useEffect, useState } from "react";
import "../style/navbar.css";

export default function Navbar() {

  const [user, setUser] = useState(null);

  useEffect(() => {

    async function fetchUser() {

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

  return (
    <header className="navbar">

      <div>
        <h2>Dashboard</h2>
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