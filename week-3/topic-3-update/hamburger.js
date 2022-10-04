// 點擊漢堡叫出導覽列
let burger=document.getElementById("burger");
let burger1=document.getElementById("burger1");
let navbar2=document.getElementById("navbar2");
let li=document.getElementById("li");
let li1=document.getElementById("li1");
let li2=document.getElementById("li2");
let li3=document.getElementById("li3");
burger.addEventListener("click",()=>{
    navbar2.style.width="50%"
})
// 點擊其他地方關閉導覽列
window.addEventListener("resize",()=>{
    if(window.innerWidth>600){
        navbar2.style.width="0%"; 
    }
})
document.body.addEventListener("click", (e)=>{
    if(window.innerWidth<=600){
        if(e.target!=navbar2 && e.target!=li&& e.target!=li1&& e.target!=li2&& e.target!=li3&&e.target!=burger1){
            navbar2.style.width="0%";    
        }    
    }
})





