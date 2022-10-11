let squareInput = document.getElementById("squareInput")
let squareHref = document.getElementById("squareHref")
let number
squareInput.addEventListener("input",function(e){
    number = e.target.value
    console.log(number)
})
squareHref.addEventListener("click",function(){
    squareHref.href=`/square/${number}`
})