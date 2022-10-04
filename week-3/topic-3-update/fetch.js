
// fetch資料

let url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
async function getdata(){
    try{
        const response = await fetch(url);
        let data = await response.json()
        console.log(data)
        return data
    }
    catch(err){
        console.log("fetch failed:",err)
    }
}

