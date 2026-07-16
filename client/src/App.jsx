import { Routes, Route } from "react-router-dom";
import AuthPage from "./pages/AuthPage.jsx";
import DashboardLayout from "./components/DashboardLayout.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import Transactions from "./pages/Transactions.jsx";
import Analytics from "./pages/Analytics.jsx";
import Ai from "./pages/AIInsights.jsx";
import Reports from "./pages/Reports.jsx";
import Settings from "./pages/Settings.jsx";
import Landing from "./pages/Landing.jsx";
import Auth from "./utils/Auth.jsx"

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing/>}/>
      <Route path="/auth" element={<AuthPage/>} />
     <Route
        element={
          <Auth>
            <DashboardLayout />
          </Auth>
        }
      > 
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