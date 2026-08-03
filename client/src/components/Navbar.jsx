import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

import "../style/navbar.css";


export default function Navbar({

    sidebarOpen,

    setSidebarOpen,

}) {


    const [user, setUser] = useState(null);

    const location = useLocation();





    useEffect(() => {


        async function fetchUser() {



            try {


                // Check Demo Mode

                const isDemo = 
                localStorage.getItem("demoMode") === "true";



                if(isDemo){


                    const demoUser = 
                    JSON.parse(
                        localStorage.getItem("demoUser")
                    );



                    setUser(demoUser);


                    return;


                }






                const token = 
                localStorage.getItem("token");



                if(!token){

                    console.log("No token found");

                    return;

                }







                const response = await fetch(


                    `${import.meta.env.VITE_API_URL}/api/users/profile`,


                    {


                        headers:{


                            Authorization:

                            `Bearer ${token}`


                        }


                    }


                );







                const data = await response.json();




                console.log(
                    "Profile Data:",
                    data
                );






                if(data.success){



                    setUser(data.user);



                    // Save user locally

                    localStorage.setItem(

                        "user",

                        JSON.stringify(data.user)

                    );


                }



            }


            catch(error){


                console.error(

                    "User Fetch Error:",

                    error

                );


            }


        }





        fetchUser();



    }, []);









    const pageDetails = {


        "/dashboard": {

            title:"Dashboard",

            icon:"ti-home",

        },



        "/transactions": {

            title:"Transactions",

            icon:"ti-receipt",

        },



        "/analytics": {

            title:"Analytics",

            icon:"ti-chart-bar",

        },



        "/ai": {

            title:"AI Insights",

            icon:"ti-sparkles",

        },



        "/reports": {

            title:"Reports",

            icon:"ti-file-text",

        },



        "/settings": {

            title:"Settings",

            icon:"ti-settings",

        },


    };








    const currentPage = 

    pageDetails[location.pathname] || {


        title:"ExpenseX",

        icon:"ti-layout-dashboard"


    };







    const userName = 

        user?.name ||

        user?.username ||

        user?.fullName ||

        "User";









    return (



        <header className="navbar">






            <div className="navbar-left">





                <button


                    className="menu-toggle"


                    onClick={()=>


                        setSidebarOpen(
                            prev=>!prev
                        )


                    }


                >


                    <i className="ti ti-menu-2"></i>


                </button>







                <h2>


                    <i 

                    className={`ti ${currentPage.icon}`}

                    ></i>


                    {currentPage.title}



                </h2>






            </div>










            <div className="navbar-right">






                <button className="icon-btn">


                    <i className="ti ti-bell"></i>


                </button>







                <div className="profile">





                    <img


                    src={

                    `https://ui-avatars.com/api/?name=${encodeURIComponent(
                        userName
                    )}`

                    }


                    alt="avatar"


                    />








                    <span>


                        {userName}



                    </span>






                </div>







            </div>






        </header>


    );

}