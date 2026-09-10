


function EditOption(id ){
    let elm = document.getElementsByClassName("ResponseSpan");
    console.log(elm)
    let el = document.getElementsByClassName("submitEdits");
    console.log(elm)
    for (let i = 0; i<el.length;i++){
        el[i].style.display = "none";
        
    }
    for (let i = 0; i<elm.length;i++){
        elm[i].setAttribute("contenteditable","false");
        elm[i].style.background = "#212529";

    }

    

    let editableField = document.getElementById(`You_${id}`).firstElementChild;

    editableField.setAttribute("contenteditable","true");
    editableField.style.background = "#505a63";

    let e= document.getElementById(`You_${id}`)
    e.children[2].style.display = "block"
    











}
export default EditOption