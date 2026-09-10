
import { useState } from 'react'
import  { useNavigate  } from 'react-router-dom'
import "./Login.css"




function SignUP() {
    const navigate = useNavigate();
    async function submitForm(event) {
        event.preventDefault(); 
        
        const formData = new FormData(event.target);
        console.log(formData);
        const API_URL = import.meta.env.VITE_BACKEND_URL
        const response = await fetch(`${API_URL}/FormMethods/SignUp/`, {
            method: 'POST',
            body: formData,
        });
        console.log("hmm");
        console.log(response);
        const result = await response.json();
        console.log(result["Vaild"]);
        
        if (result["Valid"] ===true){
            console.log("success");
            navigate(`/`);
        }
        else if(result["Valid"] === false){
            console.log("jj")
            const wrapper = document.getElementById("LogIn-SignIn-Form-Wrapper");
            wrapper.style.color =  "darkred";
            const wrapper2 = document.getElementById("errorlabel")
            wrapper2.innerText = "Error"
            


        }
        
        
        
    }
    return(
        <div id = "LogIn-SignIn-Form-Wrapper">
            <div class =  "Form">
            <h1>Create an Account</h1>
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
                <button type="submit">SignUp</button>
            </form>

            </div>
            
        </div>
       
    )
}
export default SignUP