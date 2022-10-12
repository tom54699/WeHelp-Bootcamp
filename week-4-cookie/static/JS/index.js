let squareInput = document.getElementById("squareInput")
let squareHref = document.getElementById("squareHref")
let number
let result
let regex = /[0-9]*/
squareInput.addEventListener("input",function(e){
    number = e.target.value
    result = number.match(regex)
    result = Number(result)

})
squareHref.addEventListener("click",function(){

    squareHref.href=`/square/${result}`
})


