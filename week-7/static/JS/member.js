

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
        console.log("實際的留言id",Object.keys(data)[0])
        let historyContent
        messageNode = document.querySelector(".message")
        historyContentLength = Object.keys(data).length
        for(let i=0;i<=historyContentLength-1;i++){
            historyContent = data[`${Object.keys(data)[i]}`]
            message = document.createElement("div")
            message.textContent = `${historyContent}`
            message.id = Object.keys(data)[i]
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

        // 清空input的值
        if (contentInput.value !="") {
            contentInput.value = "";
        }
        // 輸入值刪除
        content = ""

    }
    catch(err){
        console.log("fetch failed:",err)
    }
})

let deleteAll = document.getElementById("deleteAll")
deleteAll.addEventListener("click",async function(){
    let child = messageNode.lastElementChild
    while (child) { 
        messageNode.removeChild(child); 
        child = messageNode.lastElementChild; 
    } 
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
// week-7 - 查姓名功能
let nameQueryInput = document.getElementById("nameQueryInput")
let nameInputValue
nameQueryInput.addEventListener("input",function(e){
    nameInputValue = e.target.value
})

let nameQuery = document.getElementById("nameQuery")
nameQuery.addEventListener("click",async function(){
    try{
        const url = `/api/member?account=${nameInputValue}`
        const config = {
            method: "GET",
            headers: headers
        }
        let response = await fetch(url,config)
        let data = await response.json()
        console.log("姓名查詢回傳的資料",data)
        console.log("姓名查詢回傳的資料",data["data"])
        // 準備append資料
        let nameQueryNode = document.querySelector(".nameQuery")
        nameQueryResult = document.createElement("div")
        // 如果是null
        if(data["data"] == "null"){
            nameQueryResult.textContent = "查無此帳號"
            nameQueryNode.append(nameQueryResult)
        }
        else{
            nameQueryResult.textContent = `${data["data"]["name"]}`
            nameQueryNode.append(nameQueryResult)
        }
        // 清空input的值
        if (nameQueryInput.value !="") {
            nameQueryInput.value = "";
        }
        // 輸入值刪除
        nameInputValue = ""
    }
    catch(err){
        console.log("fetch failed:",err)
    }
})

// 改姓名功能
let nameUpdateInput = document.getElementById("nameUpdateInput")
let nameUpdateValue
nameUpdateInput.addEventListener("input",function(e){
    nameUpdateValue = e.target.value
})

let nameUpdate = document.getElementById("nameUpdate")
nameUpdate.addEventListener("click",async function(){
    try{
        const url = "/api/member"
        const config = {
            method: "PATCH",
            headers: headers,
            body: JSON.stringify({
                "name": `${nameUpdateValue}`
            })
        }
        let response = await fetch(url,config)
        let data = await response.json()
        console.log("姓名查詢回傳的資料",data)
        // 準備append資料
        let nameUpdateNode = document.querySelector(".nameUpdate")
        let welcomeNode = document.querySelector(".welcome")
        welcomeUpdate = document.createElement("div")
        nameUpdateResult = document.createElement("div")
        console.log(welcomeNode.childNodes)
        console.log(welcomeNode.firstElementChild)
        // 如果是error
        if(data["error"]== "true"){
            welcomeUpdate.textContent = `恭喜你${nameUpdateValue}先生/小姐，成功登入系統`
            welcomeNode.replaceChild(welcomeUpdate,welcomeNode.firstElementChild)
            nameUpdateResult.textContent = "更新失敗"
            nameUpdateNode.append(nameUpdateResult)
        }
        else{
            welcomeUpdate.textContent = `恭喜你${nameUpdateValue}先生/小姐，成功登入系統`
            welcomeNode.replaceChild(welcomeUpdate,welcomeNode.firstElementChild)
            nameUpdateResult.textContent = "更新成功"
            nameUpdateNode.append(nameUpdateResult)
        }
        // 清空input的值
        if (nameUpdateInput.value !="") {
            nameUpdateInput.value = "";
        }
        // 輸入值刪除
        nameUpdateValue = ""
    }
    catch(err){
        console.log("fetch failed:",err)
    }
})