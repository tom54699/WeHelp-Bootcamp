

let contentInput = document.getElementById("contentInput")
let contentSend = document.getElementById("contentSend")
let content;
contentInput.addEventListener("input",function(e){
    content = e.target.value
})


let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
let message;
let messageId;
let messageTime
let messageUserName;
let messageNode;
let messageContent;
contentSend.addEventListener("click",async function(){
    contentSend.href=`/message/${content}`
})

let deleteAll = document.getElementById("deleteAll")
deleteAll.addEventListener("click",async function(){
    try{
        const url = "/deleteAll"
        const config = {
            method: "DELETE",
            headers: headers,
        }
        let response = await fetch(url,config)
        let data = await response.json()
        console.log(data)
    }
    catch(err){
        console.log("fetch failed:",err)
    }
})