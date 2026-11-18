import { useState, useMemo } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import {
  FiUser,
  FiMail,
  FiLock,
  FiEye,
  FiEyeOff,
  FiAlertCircle,
  FiCheck,
  FiArrowRight,
} from "react-icons/fi";
import { signupUser } from "../data/authService";
import { disableDemoMode } from "../data/demoService";

const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

export default function Signup({ onSwitchToLogin }) {
  const navigate = useNavigate();

  // Controlled form state
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  // UI & feedback states
  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  /**
   * Calculate password strength score (0 to 4)
   */
  const passwordStrength = useMemo(() => {
    const pwd = formData.password;
    if (!pwd) return { score: 0, label: "", color: "" };

    let score = 0;
    if (pwd.length >= 8) score += 1;
    if (pwd.length >= 12) score += 1;
    if (/[A-Z]/.test(pwd) && /[a-z]/.test(pwd)) score += 1;
    if (/[0-9]/.test(pwd) || /[^A-Za-z0-9]/.test(pwd)) score += 1;

    switch (score) {
      case 1:
        return { score: 1, label: "Weak", color: "bg-red-500", text: "text-red-500" };
      case 2:
        return { score: 2, label: "Fair", color: "bg-amber-500", text: "text-amber-500" };
      case 3:
        return { score: 3, label: "Good", color: "bg-blue-500", text: "text-blue-500" };
      case 4:
        return { score: 4, label: "Strong", color: "bg-emerald-500", text: "text-emerald-500" };
      default:
        return { score: 0, label: "Too short", color: "bg-red-400", text: "text-red-400" };
    }
  }, [formData.password]);

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
    // Also clear confirmPassword error if user modifies main password
    if (name === "password" && errors.confirmPassword) {
      setErrors((prev) => ({ ...prev, confirmPassword: "" }));
    }
    // Clear global server error
    if (serverError) {
      setServerError("");
    }
  };

  /**
   * Client-side validation
   */
  const validateForm = () => {
    const validationErrors = {};

    // Name validation
    const trimmedName = formData.name.trim();
    if (!trimmedName) {
      validationErrors.name = "Full name is required.";
    } else if (trimmedName.length < 2) {
      validationErrors.name = "Name must be at least 2 characters.";
    }

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
    } else if (formData.password.length < 8) {
      validationErrors.password = "Password must be at least 8 characters long.";
    } else if (!/(?=.*[a-z])(?=.*[A-Z0-9!@#$%^&*])/.test(formData.password)) {
      validationErrors.password =
        "Password must contain a combination of letters and at least one number or symbol.";
    }

    // Confirm password validation
    if (!formData.confirmPassword) {
      validationErrors.confirmPassword = "Please confirm your password.";
    } else if (formData.password !== formData.confirmPassword) {
      validationErrors.confirmPassword = "Passwords do not match. Please re-check.";
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
      const data = await signupUser({
        name: formData.name,
        email: formData.email,
        password: formData.password,
      });

      if (data.token) {
        // Store JWT token and user profile
        localStorage.setItem("token", data.token);
        if (data.user) {
          localStorage.setItem("user", JSON.stringify(data.user));
        }

        // Clean up guest demo mode flags
        disableDemoMode();

        toast.success("Account created successfully! Welcome to ExpenseX 🎉");

        // Redirect to dashboard
        setTimeout(() => {
          navigate("/dashboard", { replace: true });
        }, 500);
      }
    } catch (err) {
      const errorMessage = err.message || "Failed to create account. Please try again.";
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

      <form onSubmit={handleSubmit} noValidate className="space-y-4">
        {/* Full Name */}
        <div>
          <label
            htmlFor="signup-name"
            className="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-200"
          >
            Full Name
          </label>
          <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
              <FiUser className="h-5 w-5" aria-hidden="true" />
            </div>
            <input
              id="signup-name"
              name="name"
              type="text"
              autoComplete="name"
              required
              disabled={isLoading}
              value={formData.name}
              onChange={handleChange}
              placeholder="e.g. Alex Johnson"
              aria-invalid={errors.name ? "true" : "false"}
              aria-describedby={errors.name ? "signup-name-error" : undefined}
              className={`block w-full rounded-xl border bg-white py-2.5 pr-4 pl-11 text-sm text-slate-900 placeholder-slate-400 transition duration-150 ease-in-out dark:bg-slate-800/80 dark:text-white dark:placeholder-slate-500 ${
                errors.name
                  ? "border-red-400 focus:border-red-500 focus:ring-2 focus:ring-red-400/40"
                  : "border-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 dark:border-slate-700 dark:focus:border-indigo-400"
              } disabled:cursor-not-allowed disabled:opacity-60`}
            />
          </div>
          {errors.name && (
            <p
              id="signup-name-error"
              role="alert"
              className="mt-1.5 flex items-center gap-1.5 text-xs font-medium text-red-600 dark:text-red-400"
            >
              <FiAlertCircle className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
              <span>{errors.name}</span>
            </p>
          )}
        </div>

        {/* Email Address */}
        <div>
          <label
            htmlFor="signup-email"
            className="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-200"
          >
            Email Address
          </label>
          <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
              <FiMail className="h-5 w-5" aria-hidden="true" />
            </div>
            <input
              id="signup-email"
              name="email"
              type="email"
              autoComplete="email"
              required
              disabled={isLoading}
              value={formData.email}
              onChange={handleChange}
              placeholder="you@example.com"
              aria-invalid={errors.email ? "true" : "false"}
              aria-describedby={errors.email ? "signup-email-error" : undefined}
              className={`block w-full rounded-xl border bg-white py-2.5 pr-4 pl-11 text-sm text-slate-900 placeholder-slate-400 transition duration-150 ease-in-out dark:bg-slate-800/80 dark:text-white dark:placeholder-slate-500 ${
                errors.email
                  ? "border-red-400 focus:border-red-500 focus:ring-2 focus:ring-red-400/40"
                  : "border-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 dark:border-slate-700 dark:focus:border-indigo-400"
              } disabled:cursor-not-allowed disabled:opacity-60`}
            />
          </div>
          {errors.email && (
            <p
              id="signup-email-error"
              role="alert"
              className="mt-1.5 flex items-center gap-1.5 text-xs font-medium text-red-600 dark:text-red-400"
            >
              <FiAlertCircle className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
              <span>{errors.email}</span>
            </p>
          )}
        </div>

        {/* Password */}
        <div>
          <div className="mb-1.5 flex items-center justify-between">
            <label
              htmlFor="signup-password"
              className="block text-sm font-semibold text-slate-700 dark:text-slate-200"
            >
              Password
            </label>
            {formData.password && (
              <span className={`text-xs font-semibold ${passwordStrength.text}`}>
                {passwordStrength.label}
              </span>
            )}
          </div>
          <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
              <FiLock className="h-5 w-5" aria-hidden="true" />
            </div>
            <input
              id="signup-password"
              name="password"
              type={showPassword ? "text" : "password"}
              autoComplete="new-password"
              required
              disabled={isLoading}
              value={formData.password}
              onChange={handleChange}
              placeholder="Minimum 8 characters"
              aria-invalid={errors.password ? "true" : "false"}
              aria-describedby={errors.password ? "signup-password-error" : undefined}
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

          {/* Visual Password Strength Bar */}
          {formData.password && (
            <div className="mt-2 flex h-1.5 w-full gap-1 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-700">
              {[1, 2, 3, 4].map((step) => (
                <div
                  key={step}
                  className={`h-full flex-1 transition-all duration-300 ${
                    step <= passwordStrength.score ? passwordStrength.color : "bg-transparent"
                  }`}
                />
              ))}
            </div>
          )}

          {errors.password && (
            <p
              id="signup-password-error"
              role="alert"
              className="mt-1.5 flex items-center gap-1.5 text-xs font-medium text-red-600 dark:text-red-400"
            >
              <FiAlertCircle className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
              <span>{errors.password}</span>
            </p>
          )}
        </div>

        {/* Confirm Password */}
        <div>
          <label
            htmlFor="signup-confirm-password"
            className="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-200"
          >
            Confirm Password
          </label>
          <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
              <FiLock className="h-5 w-5" aria-hidden="true" />
            </div>
            <input
              id="signup-confirm-password"
              name="confirmPassword"
              type={showConfirmPassword ? "text" : "password"}
              autoComplete="new-password"
              required
              disabled={isLoading}
              value={formData.confirmPassword}
              onChange={handleChange}
              placeholder="Re-enter your password"
              aria-invalid={errors.confirmPassword ? "true" : "false"}
              aria-describedby={errors.confirmPassword ? "signup-confirm-error" : undefined}
              className={`block w-full rounded-xl border bg-white py-2.5 pr-11 pl-11 text-sm text-slate-900 placeholder-slate-400 transition duration-150 ease-in-out dark:bg-slate-800/80 dark:text-white dark:placeholder-slate-500 ${
                errors.confirmPassword
                  ? "border-red-400 focus:border-red-500 focus:ring-2 focus:ring-red-400/40"
                  : formData.confirmPassword && formData.password === formData.confirmPassword
                  ? "border-emerald-400 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"
                  : "border-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 dark:border-slate-700 dark:focus:border-indigo-400"
              } disabled:cursor-not-allowed disabled:opacity-60`}
            />
            <button
              type="button"
              onClick={() => setShowConfirmPassword((prev) => !prev)}
              aria-label={showConfirmPassword ? "Hide confirm password text" : "Show confirm password text"}
              className="absolute inset-y-0 right-0 flex items-center pr-3.5 text-slate-400 hover:text-slate-600 focus:outline-none dark:hover:text-slate-200"
            >
              {showConfirmPassword ? (
                <FiEyeOff className="h-5 w-5" aria-hidden="true" />
              ) : (
                <FiEye className="h-5 w-5" aria-hidden="true" />
              )}
            </button>
          </div>
          {errors.confirmPassword && (
            <p
              id="signup-confirm-error"
              role="alert"
              className="mt-1.5 flex items-center gap-1.5 text-xs font-medium text-red-600 dark:text-red-400"
            >
              <FiAlertCircle className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
              <span>{errors.confirmPassword}</span>
            </p>
          )}
          {formData.confirmPassword && !errors.confirmPassword && formData.password === formData.confirmPassword && (
            <p className="mt-1.5 flex items-center gap-1 text-xs font-medium text-emerald-600 dark:text-emerald-400">
              <FiCheck className="h-3.5 w-3.5" aria-hidden="true" />
              <span>Passwords match</span>
            </p>
          )}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading}
          className="group relative mt-2 flex w-full items-center justify-center gap-2 rounded-xl bg-indigo-600 py-3 text-sm font-semibold text-white shadow-sm shadow-indigo-600/30 transition-all duration-200 hover:bg-indigo-700 hover:shadow-md hover:shadow-indigo-600/40 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-none active:scale-[0.99] disabled:cursor-not-allowed disabled:opacity-60 disabled:shadow-none"
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
              <span>Creating your account...</span>
            </>
          ) : (
            <>
              <span>Create Account</span>
              <FiArrowRight
                className="h-4 w-4 transition-transform duration-200 group-hover:translate-x-1"
                aria-hidden="true"
              />
            </>
          )}
        </button>
      </form>

      {/* Switch to Login footer */}
      {onSwitchToLogin && (
        <p className="mt-6 text-center text-sm text-slate-500 dark:text-slate-400">
          Already have an account?{" "}
          <button
            type="button"
            onClick={onSwitchToLogin}
            className="font-semibold text-indigo-600 hover:text-indigo-700 hover:underline focus:outline-none dark:text-indigo-400 dark:hover:text-indigo-300"
          >
            Sign in
          </button>
        </p>
      )}
    </div>
  );
}
