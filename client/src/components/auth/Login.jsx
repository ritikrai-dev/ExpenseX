import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import {
  FiMail,
  FiLock,
  FiEye,
  FiEyeOff,
  FiAlertCircle,
  FiArrowRight,
} from "react-icons/fi";
import { loginUser } from "../data/authService";
import { disableDemoMode } from "../data/demoService";

// Standard RFC 5322 email regex
const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

export default function Login({ onSwitchToSignup }) {
  const navigate = useNavigate();

  // Controlled form state
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  // UI & feedback states
  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  /**
   * Handle controlled input changes and clear field errors in real time
   */
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));

    // Clear specific field error when user starts typing
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: "" }));
    }
    // Clear global server error when user modifies form
    if (serverError) {
      setServerError("");
    }
  };

  /**
   * Client-side validation
   */
  const validateForm = () => {
    const validationErrors = {};

    // Email validation
    const trimmedEmail = formData.email.trim();
    if (!trimmedEmail) {
      validationErrors.email = "Email address is required.";
    } else if (!EMAIL_REGEX.test(trimmedEmail)) {
      validationErrors.email = "Please enter a valid email address (e.g., name@example.com).";
    }

    // Password validation
    if (!formData.password) {
      validationErrors.password = "Password is required.";
    } else if (formData.password.length < 6) {
      validationErrors.password = "Password must be at least 6 characters long.";
    }

    setErrors(validationErrors);
    return Object.keys(validationErrors).length === 0;
  };

  /**
   * Handle form submission
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setServerError("");

    if (!validateForm()) {
      return;
    }

    setIsLoading(true);

    try {
      const data = await loginUser({
        email: formData.email,
        password: formData.password,
      });

      if (data.token) {
        // Store JWT token and user info
        localStorage.setItem("token", data.token);
        if (data.user) {
          localStorage.setItem("user", JSON.stringify(data.user));
        }

        // Clean up guest / demo session flags
        disableDemoMode();

        toast.success("Welcome back! Signed in successfully 🎉");

        // Smooth redirect to dashboard
        setTimeout(() => {
          navigate("/dashboard", { replace: true });
        }, 500);
      }
    } catch (err) {
      const errorMessage = err.message || "Failed to sign in. Please verify your credentials.";
      setServerError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="w-full">
      {/* Top Server Error Alert Banner */}
      {serverError && (
        <div
          role="alert"
          className="mb-5 flex items-start gap-3 rounded-xl border border-red-200 bg-red-50/90 p-4 text-sm text-red-800 transition-all duration-200 dark:border-red-900/50 dark:bg-red-950/40 dark:text-red-300"
        >
          <FiAlertCircle className="mt-0.5 h-5 w-5 shrink-0 text-red-500" aria-hidden="true" />
          <div className="flex-1 font-medium">{serverError}</div>
        </div>
      )}

      <form onSubmit={handleSubmit} noValidate className="space-y-5">
        {/* Email Field */}
        <div>
          <label
            htmlFor="login-email"
            className="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-200"
          >
            Email Address
          </label>
          <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
              <FiMail className="h-5 w-5" aria-hidden="true" />
            </div>
            <input
              id="login-email"
              name="email"
              type="email"
              autoComplete="email"
              required
              disabled={isLoading}
              value={formData.email}
              onChange={handleChange}
              placeholder="you@example.com"
              aria-invalid={errors.email ? "true" : "false"}
              aria-describedby={errors.email ? "login-email-error" : undefined}
              className={`block w-full rounded-xl border bg-white py-2.5 pr-4 pl-11 text-sm text-slate-900 placeholder-slate-400 transition duration-150 ease-in-out dark:bg-slate-800/80 dark:text-white dark:placeholder-slate-500 ${
                errors.email
                  ? "border-red-400 focus:border-red-500 focus:ring-2 focus:ring-red-400/40"
                  : "border-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 dark:border-slate-700 dark:focus:border-indigo-400"
              } disabled:cursor-not-allowed disabled:opacity-60`}
            />
          </div>
          {errors.email && (
            <p
              id="login-email-error"
              role="alert"
              className="mt-1.5 flex items-center gap-1.5 text-xs font-medium text-red-600 dark:text-red-400"
            >
              <FiAlertCircle className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
              <span>{errors.email}</span>
            </p>
          )}
        </div>

        {/* Password Field */}
        <div>
          <div className="mb-1.5 flex items-center justify-between">
            <label
              htmlFor="login-password"
              className="block text-sm font-semibold text-slate-700 dark:text-slate-200"
            >
              Password
            </label>
          </div>
          <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
              <FiLock className="h-5 w-5" aria-hidden="true" />
            </div>
            <input
              id="login-password"
              name="password"
              type={showPassword ? "text" : "password"}
              autoComplete="current-password"
              required
              disabled={isLoading}
              value={formData.password}
              onChange={handleChange}
              placeholder="Enter your password"
              aria-invalid={errors.password ? "true" : "false"}
              aria-describedby={errors.password ? "login-password-error" : undefined}
              className={`block w-full rounded-xl border bg-white py-2.5 pr-11 pl-11 text-sm text-slate-900 placeholder-slate-400 transition duration-150 ease-in-out dark:bg-slate-800/80 dark:text-white dark:placeholder-slate-500 ${
                errors.password
                  ? "border-red-400 focus:border-red-500 focus:ring-2 focus:ring-red-400/40"
                  : "border-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 dark:border-slate-700 dark:focus:border-indigo-400"
              } disabled:cursor-not-allowed disabled:opacity-60`}
            />
            <button
              type="button"
              onClick={() => setShowPassword((prev) => !prev)}
              aria-label={showPassword ? "Hide password text" : "Show password text"}
              className="absolute inset-y-0 right-0 flex items-center pr-3.5 text-slate-400 hover:text-slate-600 focus:outline-none dark:hover:text-slate-200"
            >
              {showPassword ? (
                <FiEyeOff className="h-5 w-5" aria-hidden="true" />
              ) : (
                <FiEye className="h-5 w-5" aria-hidden="true" />
              )}
            </button>
          </div>
          {errors.password && (
            <p
              id="login-password-error"
              role="alert"
              className="mt-1.5 flex items-center gap-1.5 text-xs font-medium text-red-600 dark:text-red-400"
            >
              <FiAlertCircle className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
              <span>{errors.password}</span>
            </p>
          )}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading}
          className="group relative flex w-full items-center justify-center gap-2 rounded-xl bg-indigo-600 py-3 text-sm font-semibold text-white shadow-sm shadow-indigo-600/30 transition-all duration-200 hover:bg-indigo-700 hover:shadow-md hover:shadow-indigo-600/40 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-none active:scale-[0.99] disabled:cursor-not-allowed disabled:opacity-60 disabled:shadow-none"
        >
          {isLoading ? (
            <>
              <svg
                className="h-5 w-5 animate-spin text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                aria-hidden="true"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                />
              </svg>
              <span>Signing in...</span>
            </>
          ) : (
            <>
              <span>Sign In</span>
              <FiArrowRight
                className="h-4 w-4 transition-transform duration-200 group-hover:translate-x-1"
                aria-hidden="true"
              />
            </>
          )}
        </button>
      </form>

      {/* Switch to Signup footer */}
      {onSwitchToSignup && (
        <p className="mt-6 text-center text-sm text-slate-500 dark:text-slate-400">
          Don&apos;t have an account?{" "}
          <button
            type="button"
            onClick={onSwitchToSignup}
            className="font-semibold text-indigo-600 hover:text-indigo-700 hover:underline focus:outline-none dark:text-indigo-400 dark:hover:text-indigo-300"
          >
            Create one free
          </button>
        </p>
      )}
    </div>
  );
}
