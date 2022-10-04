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
    console.log(window.innerWidth)
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

// fetch資料
let fetch_stitle=[]
let fetch_img=[]
function getdata(){
    let url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    fetch(url).then(response=> response.json()).then(data=>{
        console.log(data)
        data_length=data["result"]["results"].length
        for(let i=0;i<data_length;i++){
            let new_fetch_stitle=data["result"]["results"][i]["stitle"]
            fetch_stitle.push(new_fetch_stitle)
            let new_fetch_img=data["result"]["results"][i]["file"].toLowerCase().split("jpg")[0]+"jpg"
            fetch_img.push(new_fetch_img)
        }
        //  產生前兩張圖文
        promotion_node=document.querySelectorAll(".promotion")
        promotionpic=document.querySelectorAll(".promotionpic")
        let image_1=document.createElement("img")
        img_1_url=fetch_img[0]
        image_1.setAttribute("src",`${img_1_url}`)
        
        let image_2=document.createElement("img")
        img_2_url=fetch_img[1]
        image_2.setAttribute("src",`${img_2_url}`)

        let text_1=document.createElement("div")
        let text_2=document.createElement("div")
        text_1.setAttribute("class","promotiontitle")
        text_2.setAttribute("class","promotiontitle")
        text_1.textContent=fetch_stitle[0]
        text_2.textContent=fetch_stitle[1]
        // 插入
        promotion_node[0].appendChild(text_1)
        promotionpic[0].appendChild(image_1)
        promotion_node[1].appendChild(text_2)
        promotionpic[1].appendChild(image_2)

        // 希望可以自動產生後面8個圖文
        function gerneratediv(){
            // 註冊
            pic_node=document.querySelectorAll(".pic")
            title_node=document.querySelectorAll(".title")
            // 建立後面8張
            for(let i=2;i<10;i++){
                pic_node=document.querySelectorAll(".pic")
                title_node=document.querySelectorAll(".title")

                let image=document.createElement("img")
                let text=document.createElement("div")

                let img_url=fetch_img[i]
                image.setAttribute("src",`${img_url}`)
                text.textContent=fetch_stitle[i]

                pic_node[i-2].appendChild(image)
                title_node[i-2].appendChild(text)

            }
        }
        gerneratediv()
    })
}
getdata()

