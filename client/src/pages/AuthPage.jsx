import { useState, useEffect } from "react";
import PasswordInput from "../assets/PasswordInput.jsx";
import { useNavigate, useSearchParams } from "react-router-dom";
import logo from "/logo1.png";
import { toast } from "react-toastify";


// ================= LOGIN =================

function LoginPanel({ onSwitch }) {

    const navigate = useNavigate();

    const [email,setEmail] = useState("");

    const [password,setPassword] = useState("");

    const [loading,setLoading] = useState(false);



    const handleSubmit = async(e)=>{

        e.preventDefault();


        try{


            setLoading(true);



            const response = await fetch(

                `${import.meta.env.VITE_API_URL}/api/auth/login`,

                {

                    method:"POST",

                    headers:{

                        "Content-Type":"application/json"

                    },

                    body:JSON.stringify({

                        email,

                        password

                    })

                }

            );



            const data = await response.json();



            if(data.token){


                localStorage.setItem(
                    "token",
                    data.token
                );


                // Remove Guest Mode

                localStorage.removeItem(
                    "demoMode"
                );

                localStorage.removeItem(
                    "demoUser"
                );

                localStorage.removeItem(
                    "demoTransactions"
                );



                toast.success(
                    "Welcome back! 🎉"
                );



                setTimeout(()=>{

                    navigate(
                        "/dashboard",
                        {
                            replace:true
                        }
                    );

                },800);



            }

            else{

                toast.error(
                    data.message
                );

            }



        }

        catch(error){

            console.log(error);

            toast.error(
                "Server error"
            );

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

<label>
Email
</label>


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


<label>
Password
</label>


<PasswordInput

id="login-password"

placeholder="Enter password"

value={password}

onChange={(e)=>setPassword(e.target.value)}

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





// ================= REGISTER =================


function RegisterPanel({onSwitch}){


const navigate = useNavigate();



const [form,setForm] = useState({

name:"",

email:"",

password:""

});



const [loading,setLoading] = useState(false);





const handleChange=(e)=>{


setForm({

...form,

[e.target.name]:e.target.value

});


};







const handleSubmit=async(e)=>{


e.preventDefault();



try{


setLoading(true);



const response = await fetch(

`${import.meta.env.VITE_API_URL}/api/auth/register`,

{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(form)

}

);



const data = await response.json();





if(data.token){


localStorage.setItem(

"token",

data.token

);



// remove guest

localStorage.removeItem(
"demoMode"
);

localStorage.removeItem(
"demoUser"
);

localStorage.removeItem(
"demoTransactions"
);



toast.success(
"Account created successfully! 🎉"
);



setTimeout(()=>{

navigate(

"/dashboard",

{

replace:true

}

);

},800);



}

else{


toast.error(
data.message
);


}



}

catch(error){


console.log(error);


toast.error(
"Server error"
);


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

<label>
Name
</label>


<div className="auth-input-wrap">


<i className="ti ti-user field-icon"/>


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


<label>
Email
</label>


<div className="auth-input-wrap">


<i className="ti ti-mail field-icon"/>


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


<label>
Password
</label>


<PasswordInput

id="register-password"

name="password"

placeholder="Create password"

value={form.password}

onChange={handleChange}

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

"Creating..."

:

"Create Account"

}


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


)


}





// ================= MAIN =================



export default function AuthPage(){


const [searchParams] = useSearchParams();


const navigate = useNavigate();



const [tab,setTab] = useState("login");





useEffect(()=>{


const mode = searchParams.get("mode");



if(mode==="register"){

setTab("register");

}

else{

setTab("login");

}



},[searchParams]);







const handleGuestMode=()=>{


localStorage.removeItem(
"token"
);



localStorage.setItem(

"demoMode",

"true"

);



localStorage.setItem(

"demoUser",

JSON.stringify({

name:"Guest User",

email:"guest@expensex.com"

})

);




toast.success(

"Welcome to Guest Mode 🚀"

);



navigate("/dashboard");


};







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







<div className="auth-tabs">


<button

className={`auth-tab ${
tab==="login" ? "active":""
}`}

onClick={()=>setTab("login")}

>

Login

</button>





<button

className={`auth-tab ${
tab==="register" ? "active":""
}`}

onClick={()=>setTab("register")}

>

Register

</button>



</div>







{

tab==="login"

?

<LoginPanel

onSwitch={()=>setTab("register")}

/>


:

<RegisterPanel

onSwitch={()=>setTab("login")}

/>

}








<div className="guest-divider">

OR

</div>





<button

className="guest-btn"

onClick={handleGuestMode}

>

Continue as Guest 🚀

</button>





</div>

</div>


)


}