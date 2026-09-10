import { useState } from 'react'
import "./Header.css"
import { useParams ,useNavigate} from 'react-router-dom';
import { Link } from 'react-router-dom';

function Header() {

    const param = useParams();
    const navigate = useNavigate();
    async function signOut(){
    const API_URL = import.meta.env.VITE_BACKEND_URL
    const response = await fetch(`${API_URL}/FormMethods/SignOut`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({id:param["Username"] })
    });
    const res= await response.json()
   

    if (res["info"] === "done"){
      navigate("/")
    }else{
      alert(res["info"])
    }
    


    }

    return(
      <div id = "Header">
          <div id  = "TitleBox">
            KRONOS 
            <img class  = "logo" src="/KRONOS.PNG" ></img>

          </div>
          <div id = "exit" onClick={signOut}>
            
            <img  class = "exit" src ="/Exit.png" >
            </img>
            
            


            
          </div>
      </div>
    )
}

export default Header
