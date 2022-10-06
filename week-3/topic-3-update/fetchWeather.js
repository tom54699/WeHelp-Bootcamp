// fetch 天氣資料


let urlWeather="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-38D05447-1373-4B83-8E52-FEE50DA80FAD&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82"
async function getWeatherdata(){
    try{
        const response = await fetch(urlWeather)
        const weatherData = await response.json()
        console.log(weatherData["records"])
        return weatherData["records"]
    }
    catch(err){
        console.log("fetch failed:",err)
    }
}

