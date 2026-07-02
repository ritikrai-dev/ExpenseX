import { useState } from "react";

export default function PasswordInput({
  id,
  ...props
}) {
  const [show, setShow] = useState(false);

  return (
    <div className="auth-input-wrap">
      <i className="ti ti-lock field-icon"></i>

      <input
        id={id}
        type={show ? "text" : "password"}
        {...props}
      />

      <button
        type="button"
        className="auth-eye-btn"
        onClick={() => setShow((prev) => !prev)}
        aria-label={show ? "Hide password" : "Show password"}
      >
        <i className={`ti ${show ? "ti-eye-off" : "ti-eye"}`}></i>
      </button>
    </div>
  );
}