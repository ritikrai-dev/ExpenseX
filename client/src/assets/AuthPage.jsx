import { useState } from "react";
import PasswordInput from "./PasswordInput";
import SocialButtons from "./SocialButtons";
import "./index.css"


// ===============================
// LOGIN COMPONENT
// ===============================

function LoginPanel({onSwitch,onSuccess}){

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


if(data.token){

localStorage.setItem(
"token",
data.token
);


onSuccess("login");

}

else{

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



<div className="auth-divider">

<span>
or continue with
</span>

</div>



<SocialButtons/>



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







// ===============================
// REGISTER COMPONENT
// ===============================

function RegisterPanel({onSwitch,onSuccess}){


const [form,setForm]=useState({

name:"",
email:"",
password:"",
confirmPassword:""

});


const [loading,setLoading]=useState(false);



const handleChange=(e)=>{

setForm({

...form,

[e.target.name]:e.target.value

});

};




const handleSubmit=async(e)=>{

e.preventDefault();



if(form.password !== form.confirmPassword){

alert("Password does not match");

return;

}



try{


setLoading(true);



const response = await fetch(

"http://localhost:5000/api/auth/register",

{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

name:form.name,

email:form.email,

password:form.password

})

}

);



const data = await response.json();



if(data.token){


localStorage.setItem(
"token",
data.token
);


onSuccess("register");


}

else{

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

<label>Name</label>


<div className="auth-input-wrap">

<i className="ti ti-user field-icon"/>


<input

name="name"

placeholder="Enter name"

value={form.name}

onChange={handleChange}

/>


</div>


</div>





<div className="auth-field">

<label>Email</label>


<div className="auth-input-wrap">


<i className="ti ti-mail field-icon"/>


<input

name="email"

type="email"

placeholder="you@example.com"

value={form.email}

onChange={handleChange}

/>


</div>


</div>





<div className="auth-field">


<label>Password</label>


<PasswordInput

id="register-password"

placeholder="Create password"

value={form.password}

onChange={handleChange}

autoComplete="new-password"

/>


</div>





<div className="auth-field">



</div>




<button
className="auth-btn"
disabled={loading}
>


{

loading

?

"Creating..."

:

"Create account"

}


</button>




<p className="auth-footer">


Already have account?


<button

type="button"

onClick={onSwitch}

>

Sign in

</button>


</p>



</form>

)

}







// ===============================
// SUCCESS MESSAGE
// ===============================


function SuccessPanel({type,onBack}){

return(

<div className="auth-success">


<h2>

{

type==="login"

?

"Login Successful"

:

"Account Created"

}

</h2>


<button

className="auth-btn"

onClick={onBack}

>

Back

</button>


</div>

)

}







// ===============================
// MAIN AUTH COMPONENT
// ===============================


export default function AuthPage(){


const [tab,setTab]=useState("login");

const [success,setSuccess]=useState(null);



return(

<div className="auth-page">


<div className="auth-card">


<h2 className="auth-brand-name">

Mini Project

</h2>



{

!success &&

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

success

?

<SuccessPanel

type={success}

onBack={()=>setSuccess(null)}

/>


:

tab==="login"

?

<LoginPanel

onSwitch={()=>setTab("register")}

onSuccess={setSuccess}

/>


:

<RegisterPanel

onSwitch={()=>setTab("login")}

onSuccess={setSuccess}

/>


}




</div>


</div>

)

}