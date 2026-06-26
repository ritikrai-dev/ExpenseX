function IconGoogle(){

return(

<svg viewBox="0 0 24 24">

<path
fill="#4285F4"
d="M21.35 12.23c0-.68-.06-1.34-.18-1.97H12v3.73h5.25a4.48 4.48 0 01-1.95 2.93v2.45h3.16c1.85-1.7 2.89-4.2 2.89-7.14z"
/>

</svg>

)

}



function IconGitHub(){

return(

<svg viewBox="0 0 24 24">

<path
fill="currentColor"
d="M12 2C6.48 2 2 6.48 2 12c0 4.42 2.87 8.17 6.84 9.5.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.61.07-.61 1 .07 1.53 1.03 1.53 1.03.89 1.53 2.34 1.09 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.95 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.02A9.56 9.56 0 0112 6.8c.85 0 1.7.11 2.5.34 1.9-1.29 2.74-1.02 2.74-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.85-2.34 4.7-4.57 4.94.36.31.68.92.68 1.86v2.75c0 .27.18.58.69.48A10 10 0 0022 12c0-5.52-4.48-10-10-10z"
/>

</svg>

)

}




export default function SocialButtons(){

return(

<div className="auth-social-row">


<button className="auth-social-btn">

<IconGoogle/>

Google

</button>


<button className="auth-social-btn">

<IconGitHub/>

Github

</button>


</div>

)

}