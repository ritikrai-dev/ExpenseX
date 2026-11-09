import { enableDemoMode } from "../components/data/demoService";

export default function Auth({ children }) {
  const token = localStorage.getItem("token");
  const demoMode = localStorage.getItem("demoMode") === "true";

  // If user is not logged in with token and not in demo mode, enable guest demo mode automatically
  // so any guest person can immediately access all layouts and features
  if (!token && !demoMode) {
    enableDemoMode();
  }

  return children;
}