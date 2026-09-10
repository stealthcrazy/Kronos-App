
import { useState } from 'react'
import  { useNavigate  } from 'react-router-dom'
import "./Login.css"





function Login() {
    const navigate = useNavigate();
    const API_URL = import.meta.env.VITE_BACKEND_URL
    async function submitForm(event) {
        event.preventDefault(); 
        
        const formData = new FormData(event.target);
        console.log(formData);
        
        const response = await fetch(`${API_URL}/FormMethods/Login/`, {
            
            method: 'POST',
            body: formData,
            redirect: 'follow'
        }); 
        console.log("hmm");
        console.log(response);
        const result = await response.json();
        console.log(result["Vaild"],result["Username"]);
        
        if (result["Vaild"] ===true){
            console.log("success");
            navigate(`/App/${result["Username"]}/Default`);
        }
        else if(result["Vaild"] === false){
            console.log("jj")
            const wrapper = document.getElementById("LogIn-SignIn-Form-Wrapper");
            wrapper.style.color =  "darkred";
            const wrapper2 = document.getElementById("errorlabel")
            wrapper2.innerText = "Incorrect Password or Username"
            


        }
        
        
        
    }
    return(
        <div id = "LogIn-SignIn-Form-Wrapper">
            <div class =  "Form">
            <h1>Login</h1>
            <form onSubmit= {submitForm} >
            
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required></input>
                <br></br>
                <br></br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required></input>
                <br></br>
                <br></br>
                <label id = "errorlabel"></label>
                <button type="submit">Login</button>
            </form>

            </div>
            
        </div>
       
    )
}
export default Login