import { useState } from "react";
import PasswordInput from "../assets/PasswordInput.jsx";
import { useNavigate } from "react-router-dom";
import logo from "/logo1.png";

// LOGIN COMPONENT

function LoginPanel({onSwitch}){
const navigate = useNavigate();
const [email,setEmail] = useState("");
const [password,setPassword] = useState("");
const [loading,setLoading] = useState(false);
const handleSubmit = async(e)=>{
e.preventDefault();
try{
setLoading(true);
const response = await fetch(
"http://localhost:5000/api/auth/login",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
email,
password
})
});
const data = await response.json();
if (data.token) {
  localStorage.setItem("token", data.token);
  navigate("/dashboard", { replace: true });
} else {
  alert(data.message);
}
}
catch(error){
console.log(error);
alert("Server error");
}
finally{
setLoading(false);
}
};
return(
<form 
className="auth-form"
onSubmit={handleSubmit}
>
<div className="auth-field">
<label>Email</label>
<div className="auth-input-wrap">
<i className="ti ti-mail field-icon"/>
<input
type="email"
placeholder="you@example.com"
value={email}
onChange={(e)=>setEmail(e.target.value)}
required
/>
</div>
</div>
<div className="auth-field">
<label>Password</label>
<PasswordInput
id="login-password"
placeholder="Enter password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
autoComplete="current-password"
required
/>
</div>
<button 
className="auth-btn"
disabled={loading}
>
{
loading
?
"Signing in..."
:
"Sign in"
}
</button>
<p className="auth-footer">
Don't have an account?
<button
type="button"
onClick={onSwitch}
>
Create one
</button>
</p>
</form>
)
}
// REGISTER COMPONENT
function RegisterPanel({ onSwitch}) {
    const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
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
    try {
      setLoading(true);
      const response = await fetch(
        "http://localhost:5000/api/auth/register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: form.name,
            email: form.email,
            password: form.password,
          }),
        }
      );
      const data = await response.json();
     if (data.token) {
        localStorage.setItem("token", data.token);
        navigate("/dashboard", { replace: true });
    } else {
  alert(data.message);
}
    } catch (error) {
      console.log(error);
      alert("Server error");
    } finally {
      setLoading(false);
    }
  };
  return (
    <form
      className="auth-form"
      onSubmit={handleSubmit}
    >
      <div className="auth-field">
        <label>Name</label>
        <div className="auth-input-wrap">
          <i className="ti ti-user field-icon" />
          <input
            name="name"
            type="text"
            placeholder="Enter your name"
            value={form.name}
            onChange={handleChange}
            required
          />
        </div>
      </div>
      <div className="auth-field">
        <label>Email</label>
        <div className="auth-input-wrap">
          <i className="ti ti-mail field-icon" />
          <input
            name="email"
            type="email"
            placeholder="you@example.com"
            value={form.email}
            onChange={handleChange}
            required
          />
        </div>
      </div>
      <div className="auth-field">
        <label>Password</label>
        <PasswordInput
  id="register-password"
  name="password"
  placeholder="Create password"
  value={form.password}
  onChange={handleChange}
  autoComplete="new-password"
  required
/>
      </div>
      <button
        className="auth-btn"
        disabled={loading}
      >
        {loading ? "Creating..." : "Create Account"}
      </button>
      <p className="auth-footer">
        Already have an account?
        <button
          type="button"
          onClick={onSwitch}
        >
          Sign in
        </button>
      </p>
    </form>
  );
}
// MAIN AUTH COMPONENT
export default function AuthPage(){
const [tab,setTab]=useState("login");
return(
<div className="auth-page">
<div className="auth-card">
<div className="auth-brand">
  <img
    src={logo}
    alt="ExpenseX Logo"
    className="auth-logo"
  />

  <div>
    <h2 className="auth-brand-name">
      ExpenseX Tracker
    </h2>
    <p className="auth-brand-tagline">
      Smart Expense Management
    </p>
  </div>
</div>
{
<div className="auth-tabs">
<button
className={`auth-tab ${
tab==="login" ? "active" : ""
}`}
onClick={()=>setTab("login")}
>
Login
</button>
<button
className={`auth-tab ${
tab==="register" ? "active" : ""
}`}
onClick={()=>setTab("register")}
>
Register
</button>
</div>
}
{
tab === "login"
?
<LoginPanel
    onSwitch={() => setTab("register")}
/>
:
<RegisterPanel
   onSwitch={() => setTab("login")}
/>
}
</div>
</div>
)
}