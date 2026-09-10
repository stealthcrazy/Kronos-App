


const getChatData = async()=>{
        
    const response = await fetch('http://127.0.0.1:8000/ChatMessages', {
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
  if (res.MessageInfo != "None"){
    for(let i = 0; i<res.MessageInfo.length ; i+=2){

      Id+=1
      setID(Id);
      addComp("You",res.info[i])
      addComp(Id,res.info[i+1])
      

      
    }
  }else{
    console.log(res.ChatInfo)
  }
  }
