import { useState, useEffect } from "react";
import { useNavigate, useSearchParams, Link } from "react-router-dom";
import { toast } from "react-toastify";
import logo from "/logo1.png";
import Login from "../components/auth/Login.jsx";
import Signup from "../components/auth/Signup.jsx";
import { enableDemoMode } from "../components/data/demoService";

export default function AuthPage({ defaultMode = "login" }) {
  const [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  // Derive active tab directly from URL search params ("login" | "signup")
  const modeParam = searchParams.get("mode");
  const tab =
    modeParam === "register" || modeParam === "signup"
      ? "signup"
      : modeParam === "login"
      ? "login"
      : defaultMode === "signup"
      ? "signup"
      : "login";

  /**
   * Switch tab and update URL query param
   */
  const handleTabChange = (newTab) => {
    setSearchParams({ mode: newTab === "signup" ? "signup" : "login" });
  };

  /**
   * Activate instant guest / demo mode without credentials
   */
  const handleGuestMode = () => {
    localStorage.removeItem("token");
    enableDemoMode();
    toast.success("Welcome to Guest Mode 🚀 Explore all features!");
    navigate("/dashboard", { replace: true });
  };

  return (
    <div className="flex min-h-screen w-full flex-col justify-center bg-slate-50 px-4 py-8 sm:px-6 lg:px-8 dark:bg-slate-950">
      <div className="mx-auto w-full max-w-md">
        {/* Brand Header */}
        <div className="mb-6 text-center sm:mb-8">
          <Link
            to="/"
            className="inline-flex items-center gap-3 transition-transform duration-200 hover:scale-105"
          >
            <img
              src={logo}
              alt="ExpenseX Logo"
              className="h-14 w-14 rounded-2xl object-cover shadow-lg shadow-indigo-500/20 ring-2 ring-indigo-500/20 sm:h-16 sm:w-16"
            />
            <div className="text-left">
              <h1 className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
                Expense<span className="text-indigo-600 dark:text-indigo-400">X</span>
              </h1>
              <p className="text-xs font-medium text-slate-500 dark:text-slate-400">
                Smart Expense Tracking & AI Insights
              </p>
            </div>
          </Link>
        </div>

        {/* Auth Card Container */}
        <div className="rounded-2xl border border-slate-200/80 bg-white/95 p-6 shadow-xl shadow-slate-200/50 backdrop-blur-sm sm:p-8 dark:border-slate-800 dark:bg-slate-900/95 dark:shadow-none">
          {/* Segmented Tab Controls */}
          <div
            role="tablist"
            aria-label="Authentication modes"
            className="mb-6 grid grid-cols-2 gap-1 rounded-xl bg-slate-100 p-1 dark:bg-slate-800/80"
          >
            <button
              type="button"
              role="tab"
              id="auth-tab-login"
              aria-selected={tab === "login"}
              aria-controls="auth-panel-login"
              onClick={() => handleTabChange("login")}
              className={`rounded-lg py-2.5 text-sm font-semibold transition-all duration-200 focus:outline-none ${
                tab === "login"
                  ? "bg-white text-slate-900 shadow-sm dark:bg-slate-700 dark:text-white"
                  : "text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white"
              }`}
            >
              Sign In
            </button>
            <button
              type="button"
              role="tab"
              id="auth-tab-signup"
              aria-selected={tab === "signup"}
              aria-controls="auth-panel-signup"
              onClick={() => handleTabChange("signup")}
              className={`rounded-lg py-2.5 text-sm font-semibold transition-all duration-200 focus:outline-none ${
                tab === "signup"
                  ? "bg-white text-slate-900 shadow-sm dark:bg-slate-700 dark:text-white"
                  : "text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white"
              }`}
            >
              Create Account
            </button>
          </div>

          {/* Form Content Area */}
          <div
            role="tabpanel"
            id={tab === "login" ? "auth-panel-login" : "auth-panel-signup"}
            aria-labelledby={tab === "login" ? "auth-tab-login" : "auth-tab-signup"}
          >
            {tab === "login" ? (
              <Login onSwitchToSignup={() => handleTabChange("signup")} />
            ) : (
              <Signup onSwitchToLogin={() => handleTabChange("login")} />
            )}
          </div>

          {/* Divider */}
          <div className="relative my-6">
            <div className="absolute inset-0 flex items-center" aria-hidden="true">
              <div className="w-full border-t border-slate-200 dark:border-slate-800" />
            </div>
            <div className="relative flex justify-center text-xs uppercase">
              <span className="bg-white px-3 font-medium text-slate-400 dark:bg-slate-900 dark:text-slate-500">
                Or explore without login
              </span>
            </div>
          </div>

          {/* Guest Mode CTA */}
          <button
            type="button"
            onClick={handleGuestMode}
            className="flex w-full items-center justify-center gap-2 rounded-xl border border-indigo-200 bg-indigo-50/60 py-3 text-sm font-semibold text-indigo-700 transition-all duration-200 hover:border-indigo-300 hover:bg-indigo-100/70 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-none dark:border-indigo-900/50 dark:bg-indigo-950/30 dark:text-indigo-300 dark:hover:bg-indigo-900/40"
          >
            <span>👤 Continue as Guest</span>
            <span className="rounded-full bg-indigo-200/80 px-2 py-0.5 text-[11px] font-bold text-indigo-800 dark:bg-indigo-900/60 dark:text-indigo-200">
              Demo
            </span>
          </button>
        </div>

        {/* Back to Home Link */}
        <p className="mt-6 text-center text-xs text-slate-500 dark:text-slate-400">
          <Link
            to="/"
            className="font-medium text-slate-600 transition-colors hover:text-indigo-600 hover:underline dark:text-slate-400 dark:hover:text-indigo-400"
          >
            ← Back to Homepage
          </Link>
        </p>
      </div>
    </div>
  );
}
