import { useState } from "react";

export default function PasswordInput({
  id,
  placeholder,
  value,
  onChange,
  autoComplete
}) {

  const [show,setShow] = useState(false);


  return (

    <div className="auth-input-wrap">

      <i className="ti ti-lock field-icon"></i>


      <input
        id={id}
        type={show ? "text" : "password"}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        autoComplete={autoComplete}
      />


      <button
        type="button"
        className="auth-eye-btn"
        onClick={()=>setShow(!show)}
      >

        <i 
          className={`ti ${
            show ? "ti-eye-off" : "ti-eye"
          }`}
        />

      </button>


    </div>

  );
}