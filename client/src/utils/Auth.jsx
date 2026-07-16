import { Navigate } from "react-router-dom";

export default function Auth({ children }) {
  const token = localStorage.getItem("token");
  const demoMode = localStorage.getItem("demoMode") === "true";

  if (!token && !demoMode) {
    return <Navigate to="/auth" replace />;
  }

  return children;
}