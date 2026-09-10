


async function UpdateMessage(Username,Chatname,CID){
    const PID =`You_${CID}`
    
    let elm = document.getElementById(PID)
    let elmText = elm.children[0].innerText
    console.log(elmText,"llle")
    elm.children[0].setAttribute("contenteditable","false");
    elm.children[0].style.background = "#212529";

    elm.children[2].style.display = "none";

    let Content;

    for(let i = 0 ; i<elmText.length;i++){
        if (elmText[i] === ":"){
            Content = elmText.slice(i+1,elmText.length);
        }

    }
    console.log(Content)
    console.log(JSON.stringify({username:Username,chatInfo:Chatname ,MessageID:`${CID}` ,prompt: Content}))
    const API_URL = import.meta.env.VITE_BACKEND_URL
    const response = await fetch(`${API_URL}/Model/EditMessages`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: Username , chatInfo: Chatname , MessageId: String(`${CID}`) ,prompt: Content })
    });
    const result = await response.json();
    console.log(result)

    const changedResponse = document.getElementById(`response_${CID}`);
    changedResponse.children[0].textContent = "1: " + result["response"];
    


}

export default UpdateMessage