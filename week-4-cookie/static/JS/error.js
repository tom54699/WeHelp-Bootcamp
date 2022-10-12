// 實作 history.api 
let hitoryButton = document.getElementById("hitoryButton")

hitoryButton.addEventListener("click",lastPage)

function lastPage(){
    history.go(-1)
}