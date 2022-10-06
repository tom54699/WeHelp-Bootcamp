

const main = async () => {
    weatherData = await getWeatherdata()
    console.log(weatherData)
    let location = weatherData["location"][0]["locationName"]
    console.log(location)
    let time = weatherData["location"][0]["weatherElement"][0]["time"][0]["startTime"].slice(0,16)+" ~ "+weatherData["location"][0]["weatherElement"][0]["time"][0]["endTime"].slice(10,16)
    console.log(time)
    let wx = weatherData["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"]
    console.log(wx)
    let pop = weatherData["location"][0]["weatherElement"][1]["time"][0]["parameter"]["parameterName"] + " %"
    console.log("降雨機率" ,pop)
    let MinT = weatherData["location"][0]["weatherElement"][2]["time"][0]["parameter"]["parameterName"] + " °C" 
    let MaxT = weatherData["location"][0]["weatherElement"][4]["time"][0]["parameter"]["parameterName"] + " °C"
    console.log("最低溫和最高溫為",MinT,MaxT)
    let ci = weatherData["location"][0]["weatherElement"][3]["time"][0]["parameter"]["parameterName"]
    console.log("體感舒適度",ci)
    weatherText = `${location} ${time} ${wx} 降雨機率${pop} 最低溫:${MinT} 最高溫${MaxT} ${ci}`
    let weatherNode = document.querySelector(".weather")
    let weather = document.createElement("div")
    weather.textContent=weatherText
    weatherNode.appendChild(weather)
}

main()

