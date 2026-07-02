import "../style/navbar.css";

export default function Navbar() {
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
            src="https://ui-avatars.com/api/?name=Ritik"
            alt="avatar"
          />

          <span>Ritik</span>

        </div>

      </div>

    </header>
  );
}

