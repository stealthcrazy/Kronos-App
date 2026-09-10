import { useState , useEffect , useContext } from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import "./ContentBox.css"
import getPredictions from './Predictions/GetPredictions';

import { ChatContext,MenuContext } from './App';
import EditOption from './Functions/setEditable';
import UpdateMessage from './Functions/UpdateMessages';

function ContentBox() {
    

    let [Comp , setComp] = useState([])
    let [result, setResult] = useState({});
    let [Id , setID] = useState(0)
    let { ChatState , setChatState} = useContext(ChatContext);
    const { MenuState,setMenuState } = useContext(MenuContext);
    const navigate = useNavigate();
    const API_URL = import.meta.env.VITE_BACKEND_URL
    const param = useParams()
    function textVanish(){
      let a = document.getElementById("TextBox")

      

      if (a.dataset.flag === "notEdited"){
         
          console.log(a.innerText ,a.innerHTML )
          
           a.innerText = "";/* setting inner Text ot "" removes all child nodes */
          console.log(a.innerText ,a.innerHTML )
          a.dataset.flag = "Edited";

      }
      
      
    }


    function addComp(id,text){
        //const Response = <div id = {`response_${id}`} class = "ResponseBox"></div>
        console.log(id)
        let Response;
        if (id != "You"){
          console.log("hi")
          Response = <div id = {`response_${id}`}  class = "ResponseBox"  > 
          <span contenteditable = "false" class = "ResponseSpan" >{id}: {text} </span> 
        </div>
          
        }
        else{
          const CID = Id;
          Response = <div id = {`You_${Id}`}  class = "ResponseBox"  > 
          
          <span contenteditable = "false" class = "ResponseSpan" >{id}: {text} </span> <div class  = "edit-prompt-image-container" onClick={()=>EditOption(CID) }> <img  class = "edit" src ="/Edit.png" ></img></div>
          <div class= "submitEdits">
            <button id = "Editsend" onClick={()=>UpdateMessage(param["Username"],param["Chat"],CID)}>Submit</button>

          </div>

          </div>
          
        }
        
        Comp=[...Comp,Response]
        setComp(Comp)
        
    }
    async function getGPTResponse() {
      
      console.log(param["Chat"])
      document.getElementById("Prediction").innerText = ""
      const inputText = document.getElementById("TextBox").innerText;
      
      const button = document.getElementById("send");
      document.getElementById("TextBox").innerText = "Message KRONOS"
      document.getElementById("TextBox").dataset.flag = "notEdited"
      button.disabled = true;

      console.log(inputText)
      addComp("You:",inputText);
      const response = await fetch(`${API_URL}/Model/User/3/Prompts/4`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username:param["Username"],chatInfo:param["Chat"] ,MessageId:`${Id+1}` ,prompt: inputText })
      });
      console.log({ username:param["Username"],chatInfo:param["Chat"] ,prompt: inputText })
      const result = await response.json();
      console.log(result)
      
      Id+=1
      setID(Id);
      addComp(Id , result.response);
      console.log("Success in Request"+result.chatname)
      button.disabled = false;
      setMenuState(0)
      if (param["Chat"] === "Default"){
        navigate(`/App/${param["Username"]}/${result.chatname}`, { replace: true });

      }
      
    }
    useEffect(()=>{
      console.log(ChatState + "---")
      
      
      if (ChatState ==1){
        const getChatData = async()=>{
        
          const response = await fetch(`${API_URL}/ChatMethods/ChatMessages`, {
            method: 'POST',
            headers: {
                  'Content-Type': 'application/json'
              },
            body: JSON.stringify({username:param["Username"],chatname:param["Chat"]})
        });
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
        Comp=[]
        Id = 0
        if (res.MessageInfo != "None"){
          for(let i = 0; i<res.MessageInfo.length ; i+=2){
      
            Id+=1
            setID(Id);
            addComp("You",res.MessageInfo[i])
            addComp(Id,res.MessageInfo[i+1])
            
      
            
          }
        }else{
          console.log("here")
          Comp=[]
          Id = 0
          setID(Id)
          setComp(Comp)
          

        }
        setChatState(0)
        
        
        
        
      }
      
  
      getChatData()
      }
      
      
    
    },[ChatState , MenuState]);
    


    return(
      <div id = "ContentBoxWrapper">
          <div id = "ResponseComponents">
          {Comp}
          </div>
          
          <div id = "TextField">
            <span id= "TextBox" contentEditable = "true" onClick={textVanish} data-flag ="notEdited" onKeyUp={()=>getPredictions()}>Message KRONOS <span contenteditable='false' id = 'Prediction'></span> </span>
            
            <button id = "send" onClick={getGPTResponse}> <img  class = "sendImg" src ="/Send.png" ></img></button>
          </div>
      </div>
    )
}






export default ContentBox