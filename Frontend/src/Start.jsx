
import { useState } from 'react'
import  { useNavigate  } from 'react-router-dom'
import "./Start.css"
import { Link } from 'react-router-dom'





function Start() {
    
    return(

        <div id = "Content">
            <div id = "info">
            <div id = "Top">
            <Link id="Link" to={{
                pathname: `/Login`,
       
        
            }}> Login</Link>
            <Link id="Link" to={{
                pathname: `/SignUp`,
       
        
            }}> Sign Up</Link>

            </div>

            <div id  = "text">
                <p> Hey there! Welcome to Kronos, your go-to conversational chatbot.
            <br></br>
            Looking for a quick chat then login to your account or create one today 
            <br></br>
            <br></br>
            Once you're logged in, Kronos is ready to reply to you messages.
            <br></br>
            Feel free to explore and start a conversation anytime.
            <br></br>
            Need more info  Go ahead and dive in. We can’t wait for you try our to chat!
                </p>
            </div>

            </div>

            
            
        </div>
       
    )
}
export default Start