import { useState } from 'react'
import "./TextInput.css"

function TextField() {
    return(
      <div id = "TextField">
            <div id = "TextBox" contentEditable = "true">Message KRONOS</div>
            <button id = "send" onClick={getGPTResponse}></button>
      </div>
    )
}
function Log(){
    const E = document.getElementById("TextBox")
    console.log(E.innerText)
}

async function getGPTResponse() {
  const inputText = document.getElementById("TextBox").innerText;
  console.log(inputText)
  const response = await fetch('http://127.0.0.1:8000/User/3/Prompts/4', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: inputText })
  });

  const result = await response.json();
  document.getElementById('response').textContent = result.response;
  console.log("Success in Request")
  
}

export default TextField
