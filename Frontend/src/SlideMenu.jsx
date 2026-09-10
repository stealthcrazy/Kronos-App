import { useState , useEffect, useContext } from 'react'
import "./SlideMenu.css"
import { useParams ,useNavigate} from 'react-router-dom';
import { Link } from 'react-router-dom';
import { ChatContext, MenuContext } from './App';


function SlideMenu() {

  let [Comp , setComp] = useState([])
  let [result, setResult] = useState({});
  let [Id , setID] = useState(0)
  const { ChatState,setChatState } = useContext(ChatContext);
  const { MenuState,setMenuState } = useContext(MenuContext);
  const navigate = useNavigate();
  const API_URL = import.meta.env.VITE_BACKEND_URL

  
  const param = useParams()

  function DisplayOptions(text){
    let  B = document.getElementById(text);
    if (B.style.display ==="none"){
      B.style.display = "Block"
    }else{
      B.style.display = "none"
    }

  }

  async function deleteChat(text){
    
    console.log(text)
    const response = await fetch(`${API_URL}/ChatMethods/DeleteChats/`, {
      method: 'POST',
      headers: {
            'Content-Type': 'application/json'
        },
      body: JSON.stringify({username:param["Username"],chatname:text})
    })
    const res= await response.json()
    console.log(res["status"])
    setID(0)
    setComp([])
    setMenuState(0)
    navigate(`/App/${param["Username"]}/Default`, { replace: true });
    setChatState(1)

  }
  
  function addComp(id,text){
      //const Response = <div id = {`response_${id}`} class = "ResponseBox"></div>
      
      const Response = <div class = "chats_menu_box"><Link id = {`chats_menu_box_${id}`}   onClick={()=>setChatState(1)} to={{
        pathname: `/App/${param["Username"]}/${text}`,
       
        
      }}> 
      <div>{id}: {text}  </div>
      
      </Link>
      <div class = "ButtonMenu" onClick={()=>DisplayOptions(text)}>
        <div class = "Circle" ></div> 
        <div class = "Circle" ></div>
        < div class = "Circle" ></div>
      </div>
      <div id = {text}class ="MenuOptions">
        <button id = {text}  class ="delete" onClick ={()=>deleteChat(text)}>Delete</button>
      </div> 
      </div>
      Comp=[...Comp,Response,]
      setComp(Comp)
      
      
  }
  useEffect(()=>{
    const getChatData = async()=>{
      
      const response = await fetch(`${API_URL}/ChatMethods/ChatNames`, {
        method: 'POST',
        headers: {
              'Content-Type': 'application/json'
          },
        body: JSON.stringify({username:param["Username"],chatname:param["Chat"]})
    });
    console.log(MenuState)
    
    if (MenuState == 0){
        Comp=[]
        Id=0
        setComp(Comp)
        setID(Id)
        setMenuState(1)
        //console.log(response)
        const res= await response.json()
        setResult(res)
        //console.log(res);
        /*if(result.info !="True"){
          navigate("/")
        }*/
        //console.log(res.info.length)
        //console.log(param)
        console.log(res)
        
        console.log(res.ChatInfo)
        if (res.ChatInfo.length != 0){
          for(let i =0 ; i< res.ChatInfo.length;i++){
            Id+=1;
            setID(Id)
            addComp(Id,res.ChatInfo[i])

          }
        }
        
      }
 
  }

  getChatData()
  
  },[MenuState]);


    return(
      <div id = "SlideMenuWrapper">
        <div id ="createChat">
        <Link  onClick={()=>setChatState(1)} to = {{pathname: `/App/${param["Username"]}/Default`}}>Create new chat</Link>
        </div>
        
        {Comp}
      </div>
    )
}

export default SlideMenu
