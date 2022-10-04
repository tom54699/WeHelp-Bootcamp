

let fetch_stitle=[]
let fetch_img=[]

getdata().then(data=>{
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

    // 註冊
    let pic_node=document.querySelectorAll(".pic")
    let title_node=document.querySelectorAll(".title")
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
    // 希望可以自動產生後面8個圖文
    // 註冊
    let blockbox_node=document.querySelector(".blockbox")
    let static_block_node=document.querySelectorAll(".block")
    let star_node=document.querySelectorAll(".star")
    function gerneratediv(){
        static_block_node=document.querySelectorAll(".block")
        console.log(static_block_node)
        if (static_block_node.length <= 42){
            // 建立一組8張的block
            for(let i=static_block_node.length;i<static_block_node.length+8;i++){
                let block=document.createElement("div")
                block.setAttribute("class","block")
                blockbox_node.appendChild(block)
                let block_node=document.querySelectorAll(".block")
                console.log(block_node)

                let pic=document.createElement("div")
                pic.setAttribute("class","pic")
                block_node[i].appendChild(pic)
                pic_node=document.querySelectorAll(".pic")

                let title=document.createElement("div")
                title.setAttribute("class","title")
                block_node[i].appendChild(title)
                title_node=document.querySelectorAll(".title")

                let star=document.createElement("div")
                star.setAttribute("class","star")
                block_node[i].appendChild(star)
                star_node=document.querySelectorAll(".star")

                let image=document.createElement("img")
                let image_star=document.createElement("img")
                let text=document.createElement("div")


                let img_url=fetch_img[i]
                image.setAttribute("src",`${img_url}`)
                image_star.setAttribute("src","1142010.png")
                text.textContent=fetch_stitle[i]

                pic_node[i].appendChild(image)
                star_node[i].appendChild(image_star)
                title_node[i].appendChild(text)
                
            }
        }else{
            console.log("後面沒圖了")
        }
    }
 
    // Load more
    let load = document.getElementById("load")
    load.addEventListener("click",gerneratediv)
})



