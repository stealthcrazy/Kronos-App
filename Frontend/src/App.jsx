import { useState , useEffect , createContext } from 'react'
import { useParams } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import './App.css'
import Header from './Header.jsx'
import SlideMenu from './SlideMenu.jsx'
import ContentBox from './ContentBox.jsx'


export const ChatContext = createContext(null);
export const MenuContext = createContext(null);

function App() {
  const param = useParams()
  const navigate = useNavigate()
  const API_URL = import.meta.env.VITE_BACKEND_URL
  
  let [result, setResult] = useState({});
  let [ChatState, setChatState] = useState(0);
  let [MenuState, setMenuState] = useState(0);
  
  
    


  
  
  useEffect(()=>{
    const getAuth = async()=>{
      
      const response = await fetch(`${API_URL}/AuthenticationMethods/Authcheck`, {
        method: 'POST',
        headers: {
              'Content-Type': 'application/json'
          },
        body: JSON.stringify({ id: param["Username"] })
    });
    console.log(response)
    const res= await response.json()
    setResult(res)
    console.log(result);
    /*if(result.info !="True"){
      navigate("/")
    }*/
    if (param["Chat"]!="Default"){
        setChatState(1)
      }
    
    }
    getAuth()
    
    },[]);
    if (result.info  =="True"){
      return(
        
        <div id = "MainGridWrapper">
          <Header/>
          
            <ChatContext.Provider value = {{ChatState,setChatState}}>
              <MenuContext.Provider value={{MenuState,setMenuState}}>
                <SlideMenu/>
                
                
                <ContentBox/> 
                </MenuContext.Provider>
            </ChatContext.Provider>
           
        </div> 
      )
    }else{
      navigate("/")
    }
    
    
    

  
  }
export default App
