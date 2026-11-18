import { useState, useEffect } from "react";
import PasswordInput from "../assets/PasswordInput.jsx";
import { useNavigate, useSearchParams } from "react-router-dom";
import logo from "/logo1.png";
import { toast } from "react-toastify";
import { enableDemoMode } from "../components/data/demoService";

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const getApiUrl = () =>
  (import.meta.env.VITE_API_URL || "http://localhost:5000").replace(/\/$/, "");

// ================= LOGIN PANEL =================
function LoginPanel({ onSwitch }) {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const cleanEmail = email.trim();
    if (!cleanEmail || !password) {
      toast.error("Please enter email and password");
      return;
    }

    if (!EMAIL_REGEX.test(cleanEmail)) {
      toast.error("Please enter a valid email address");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(`${getApiUrl()}/api/auth/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: cleanEmail,
          password,
        }),
      });

      const data = await response.json();

      if (data.token) {
        localStorage.setItem("token", data.token);
        if (data.user) {
          localStorage.setItem("user", JSON.stringify(data.user));
        }

        // Clear guest mode so real account data loads
        localStorage.removeItem("demoMode");
        localStorage.removeItem("demoUser");
        localStorage.removeItem("demoTransactions");

        toast.success("Welcome back! 🎉");

        setTimeout(() => {
          navigate("/dashboard", { replace: true });
        }, 600);
      } else {
        toast.error(data.message || "Invalid credentials");
      }
    } catch (error) {
      console.error("Login Error:", error);
      toast.error("Cannot connect to server. Please check your backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="auth-form" onSubmit={handleSubmit}>
      <div className="auth-field">
        <label htmlFor="login-email">Email</label>
        <div className="auth-input-wrap">
          <i className="ti ti-mail field-icon" />
          <input
            id="login-email"
            type="email"
            placeholder="you@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            autoComplete="email"
            required
          />
        </div>
      </div>

      <div className="auth-field">
        <label htmlFor="login-password">Password</label>
        <PasswordInput
          id="login-password"
          placeholder="Enter password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          autoComplete="current-password"
          required
        />
      </div>

      <button className="auth-btn" disabled={loading} type="submit">
        {loading ? "Signing in..." : "Sign in"}
      </button>

      <p className="auth-footer">
        Don't have an account?
        <button type="button" onClick={onSwitch}>
          Create one
        </button>
      </p>
    </form>
  );
}

// ================= REGISTER / SIGNUP PANEL =================
function RegisterPanel({ onSwitch }) {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const cleanName = form.name.trim();
    const cleanEmail = form.email.trim();

    if (!cleanName || !cleanEmail || !form.password) {
      toast.error("Please fill in all required fields");
      return;
    }

    if (!EMAIL_REGEX.test(cleanEmail)) {
      toast.error("Please enter a valid email address");
      return;
    }

    if (form.password.length < 6) {
      toast.error("Password must be at least 6 characters");
      return;
    }

    if (form.confirmPassword && form.password !== form.confirmPassword) {
      toast.error("Passwords do not match");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(`${getApiUrl()}/api/auth/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: cleanName,
          email: cleanEmail,
          password: form.password,
        }),
      });

      const data = await response.json();

      if (data.token) {
        localStorage.setItem("token", data.token);
        if (data.user) {
          localStorage.setItem("user", JSON.stringify(data.user));
        }

        // Clear guest mode
        localStorage.removeItem("demoMode");
        localStorage.removeItem("demoUser");
        localStorage.removeItem("demoTransactions");

        toast.success("Account created successfully! 🎉");

        setTimeout(() => {
          navigate("/dashboard", { replace: true });
        }, 600);
      } else {
        toast.error(data.message || "Registration failed");
      }
    } catch (error) {
      console.error("Register Error:", error);
      toast.error("Cannot connect to server. Please check your backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="auth-form" onSubmit={handleSubmit}>
      <div className="auth-field">
        <label htmlFor="register-name">Name</label>
        <div className="auth-input-wrap">
          <i className="ti ti-user field-icon" />
          <input
            id="register-name"
            name="name"
            type="text"
            placeholder="Enter your name"
            value={form.name}
            onChange={handleChange}
            autoComplete="name"
            required
          />
        </div>
      </div>

      <div className="auth-field">
        <label htmlFor="register-email">Email</label>
        <div className="auth-input-wrap">
          <i className="ti ti-mail field-icon" />
          <input
            id="register-email"
            name="email"
            type="email"
            placeholder="you@example.com"
            value={form.email}
            onChange={handleChange}
            autoComplete="email"
            required
          />
        </div>
      </div>

      <div className="auth-field">
        <label htmlFor="register-password">Password</label>
        <PasswordInput
          id="register-password"
          name="password"
          placeholder="Create password (min 6 chars)"
          value={form.password}
          onChange={handleChange}
          autoComplete="new-password"
          required
        />
      </div>

      <div className="auth-field">
        <label htmlFor="register-confirm-password">Confirm Password</label>
        <PasswordInput
          id="register-confirm-password"
          name="confirmPassword"
          placeholder="Confirm password"
          value={form.confirmPassword}
          onChange={handleChange}
          autoComplete="new-password"
          required
        />
      </div>

      <button className="auth-btn" disabled={loading} type="submit">
        {loading ? "Creating..." : "Create Account"}
      </button>

      <p className="auth-footer">
        Already have an account?
        <button type="button" onClick={onSwitch}>
          Sign in
        </button>
      </p>
    </form>
  );
}

// ================= MAIN AUTH PAGE =================
export default function AuthPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  const [tab, setTab] = useState(() => {
    const mode = searchParams.get("mode");
    return mode === "register" || mode === "signup" ? "register" : "login";
  });

  useEffect(() => {
    const mode = searchParams.get("mode");
    if (mode === "register" || mode === "signup") {
      setTab("register");
    } else if (mode === "login") {
      setTab("login");
    }
  }, [searchParams]);

  const handleGuestMode = () => {
    localStorage.removeItem("token");
    enableDemoMode();
    toast.success("Welcome to Guest Mode 🚀");
    navigate("/dashboard");
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-brand">
          <img src={logo} alt="ExpenseX Logo" className="auth-logo" />
          <div>
            <h2 className="auth-brand-name">ExpenseX Tracker</h2>
            <p className="auth-brand-tagline">Smart Expense Management</p>
          </div>
        </div>

        <div className="auth-tabs">
          <button
            className={`auth-tab ${tab === "login" ? "active" : ""}`}
            onClick={() => setTab("login")}
            type="button"
          >
            Login
          </button>
          <button
            className={`auth-tab ${tab === "register" ? "active" : ""}`}
            onClick={() => setTab("register")}
            type="button"
          >
            Register
          </button>
        </div>

        {tab === "login" ? (
          <LoginPanel onSwitch={() => setTab("register")} />
        ) : (
          <RegisterPanel onSwitch={() => setTab("login")} />
        )}

        <div className="guest-divider">OR</div>

        <button className="guest-btn" onClick={handleGuestMode} type="button">
          Continue as Guest 🚀
        </button>
      </div>
    </div>
  );
}
