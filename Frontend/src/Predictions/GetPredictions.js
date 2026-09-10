


async function getPredictions(){
    if (document.getElementById("Prediction")){
        document.getElementById("Prediction").remove()
        console.log( document.getElementById("TextBox").innerHTML)
    }
    
    const selection = window.getSelection();
    const rng = selection.getRangeAt(0);
    const Offset =  rng.startOffset;
    console.log(rng.startOffset , rng.endOffset)
    const span = document.createElement('span');
    span.id = 'Prediction';
    span.contentEditable = 'false';

    rng.insertNode(span)
    rng.collapse(true)

    
    


    //console.log(document.getElementById("TextBox").firstChild +" kj",Offset,rng)

    





   
    
   
    
    
    
    let text = document.getElementById("TextBox").innerText;
    console.log(text);
    const API_URL = import.meta.env.VITE_BACKEND_URL
    const response = await fetch(`${API_URL}/MarkovChains/ChainedComplete`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({Text:text})
    });

    const result = await response.json();
    console.log(result)
    document.getElementById('Prediction').innerText = " " +result["Prediction"]+" " ;
    
    

    


}

export default getPredictions;
