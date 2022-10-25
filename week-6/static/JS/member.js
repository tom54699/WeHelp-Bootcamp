

let contentInput = document.getElementById("contentInput")
let contentSend = document.getElementById("contentSend")
let content;
contentInput.addEventListener("input",function(e){
    content = e.target.value
})

let historyContentLength;
async function getMessage(){
    try{
        let response = await fetch("/getMessage")
        let data = await response.json()
        console.log("歷史資料",data)
        let historyContent
        messageNode = document.querySelector(".message")
        historyContentLength = Object.keys(data).length
        for(let i=1;i<=historyContentLength;i++){
            historyContent = data[`message${i}`]
            message = document.createElement("div")
            message.textContent = `${historyContent}`
            message.id = i
            messageNode.prepend(message)
        }
    }
    catch(err){
        console.log("fetch failed:",err)
    }
}
getMessage()

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
    console.log("fetch執行")
    try{
        const url = "/message"
        const config = {
            method: "POST",
            headers: headers,
            body: JSON.stringify({"content":content})
        }
        let response = await fetch(url,config)
        let data = await response.json()
        console.log(data)
        console.log(data["message_id"])
        // 新增留言
        messageId = data["message_id"]
        messageContent = data["content"]
        messageUserName = data["name"]
        messageTime = data["time"]
        messageNode = document.querySelector(".message")
        message = document.createElement("div")
        message.id = messageId
        console.log(message)
        console.log(messageId)
        message.textContent = `${messageUserName}: ${messageContent}`
        messageNode.prepend(message)
        if (contentInput.value !="") {
            contentInput.value = "";
        }

    }
    catch(err){
        console.log("fetch failed:",err)
    }
})
