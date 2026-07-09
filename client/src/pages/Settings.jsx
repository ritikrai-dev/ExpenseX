import { useEffect, useState } from "react";
import "../style/setting.css";
export default function Settings() {

    const [user, setUser] = useState({

        name: "",

        email: ""

    });

    const [passwords, setPasswords] = useState({

    currentPassword: "",

    newPassword: "",

    confirmPassword: ""

});

    useEffect(() => {

        fetchProfile();

    }, []);

    async function fetchProfile() {

        const response = await fetch(

            `${import.meta.env.VITE_API_URL}/api/users/profile`,

            {

                headers: {

                    Authorization:
                        `Bearer ${localStorage.getItem("token")}`

                }

            }

        );

        const data = await response.json();

        setUser(data.user);

    }

    async function handleSubmit(e) {

        e.preventDefault();

        const response = await fetch(

            `${import.meta.env.VITE_API_URL}/api/users/profile`,

            {

                method: "PUT",

                headers: {

                    "Content-Type": "application/json",

                    Authorization:
                        `Bearer ${localStorage.getItem("token")}`

                },

                body: JSON.stringify(user)

            }

        );

        const data = await response.json();

        alert(data.message);

    }

    async function handlePasswordUpdate(e){

    e.preventDefault();

    const response = await fetch(

        `${import.meta.env.VITE_API_URL}/api/users/change-password`,

        {

            method:"PUT",

            headers:{

                "Content-Type":"application/json",

                Authorization:`Bearer ${localStorage.getItem("token")}`

            },

            body:JSON.stringify(passwords)

        }

    );

    const data = await response.json();

    alert(data.message);

    if(data.success){

        setPasswords({

            currentPassword:"",

            newPassword:"",

            confirmPassword:""

        });

    }

}
    return (
<>
        <form
            className="settings-form"
            onSubmit={handleSubmit}
        >

            <h2>Profile Settings</h2>

            <input

                type="text"

                value={user.name}

                onChange={(e)=>

                    setUser({

                        ...user,

                        name:e.target.value

                    })

                }

            />

            <input

                type="email"

                value={user.email}

                onChange={(e)=>

                    setUser({

                        ...user,

                        email:e.target.value

                    })

                }

            />

            <button
                className="primary-btn"
            >

                Save Changes

            </button>

        </form>
<br></br>
        <form

className="settings-form"

onSubmit={handlePasswordUpdate}

>

<h2>🔒 Change Password</h2>

<input

type="password"

placeholder="Current Password"

value={passwords.currentPassword}

onChange={(e)=>

setPasswords({

...passwords,

currentPassword:e.target.value

})

}

/>

<input

type="password"

placeholder="New Password"

value={passwords.newPassword}

onChange={(e)=>

setPasswords({

...passwords,

newPassword:e.target.value

})

}

/>

<input

type="password"

placeholder="Confirm Password"

value={passwords.confirmPassword}

onChange={(e)=>

setPasswords({

...passwords,

confirmPassword:e.target.value

})

}

/>

<button className="primary-btn">

Update Password

</button>

</form>
</>
    );

}