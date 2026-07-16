import "./Hero.css";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { getDashboard} from "../data/demoService.js";

export default function Hero() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

function handleDemo() {
    getDashboard();
    navigate("/dashboard");
}
  return (
    <section className="hero" id="home">

      <div className="hero-bg-circle hero-circle-1"></div>
      <div className="hero-bg-circle hero-circle-2"></div>

      <div className="hero-content">

        <span className="hero-badge">
          🚀 AI Powered Personal Finance Platform
        </span>

        <h1>
          Manage Your Money
          <br />
          <span>Smarter with AI</span>
        </h1>

        <p>
          Track your income and expenses, visualize your spending,
          generate AI-powered financial insights, and export
          professional reports—all in one beautiful dashboard.
        </p>

        <div className="hero-buttons">

          <Link
            to="/auth?mode=register"
            className="hero-btn primary"
          >
            Get Started Free
          </Link>

          <button
    className="secondary-btn"
    onClick={handleDemo}
>
    Try Demo
</button>

        </div>

        <div className="hero-trust">

          <div>
            <i className="ti ti-shield-lock"></i>
            Secure JWT
          </div>

          <div>
            <i className="ti ti-sparkles"></i>
            AI Powered
          </div>

          <div>
            <i className="ti ti-device-mobile"></i>
            Responsive
          </div>

        </div>

      </div>

      <div className="hero-preview">

        <img
          src="/image.png"
          alt="ExpenseX Dashboard"
        />

      </div>

    </section>
  );
}