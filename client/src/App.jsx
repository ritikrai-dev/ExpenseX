import { Routes, Route } from "react-router-dom";

import AuthPage from "./pages/AuthPage.jsx";
import DashboardLayout from "./components/DashboardLayout.jsx";

import Dashboard from "./pages/Dashboard.jsx";
import Transactions from "./pages/Transactions.jsx";
import Analytics from "./pages/Analytics.jsx";
import Ai from "./pages/AIInsights.jsx";
import Reports from "./pages/Reports.jsx";
import Settings from "./pages/Setting.jsx";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<AuthPage/>} />

      <Route element={<DashboardLayout />}>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/transactions" element={<Transactions/>} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/ai" element={<Ai/>}/>
        <Route path="/reports" element={<Reports />} />
        <Route path="/settings" element={<Settings />} />
      </Route>
    </Routes>
  );
}