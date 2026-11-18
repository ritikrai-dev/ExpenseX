import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { enableDemoMode } from "../data/demoService";

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const closeMenu = () => setMenuOpen(false);

  const handleGuestLogin = () => {
    enableDemoMode();
    navigate("/dashboard");
  };

  return (
    <header className={`landing-navbar ${scrolled ? "scrolled" : ""}`}>
      <div className="container navbar-container">
        <Link to="/" className="logo">
          <img src="/logo1.png" alt="ExpenseX" />
          <span>ExpenseX</span>
        </Link>

        <nav className={`nav-links ${menuOpen ? "active" : ""}`}>
          <a href="#home" onClick={closeMenu}>
            Home
          </a>
          <a href="#features" onClick={closeMenu}>
            Features
          </a>
          <a href="#about" onClick={closeMenu}>
            About
          </a>
        </nav>

        <div className="nav-buttons">
          <button
            onClick={handleGuestLogin}
            className="guest-login-btn"
            style={{
              background: "transparent",
              border: "1.5px solid #4f46e5",
              color: "#4f46e5",
              padding: "7px 14px",
              borderRadius: "8px",
              fontWeight: "600",
              cursor: "pointer",
              fontSize: "0.9rem",
              transition: "all 0.2s ease",
            }}
          >
            👤 Guest Login
          </button>

          <Link to="/auth?mode=login" className="login-btn">
            Login
          </Link>

          <Link to="/auth?mode=register" className="primary-btn">
            Get Started
          </Link>
        </div>

        <button
          className="menu-btn"
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Toggle navigation"
        >
          <i className={`ti ${menuOpen ? "ti-x" : "ti-menu-2"}`}></i>
        </button>
      </div>
    </header>
  );
}