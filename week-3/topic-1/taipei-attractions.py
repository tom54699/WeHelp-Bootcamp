import urllib.request as request
import json

src = " https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json "
with request.urlopen(src) as response:
    data = json.load(response)
data_len=len(data["result"]["results"])


for x in range(data_len):
    xpostDate=data["result"]["results"][x]["xpostDate"][0:4]
    if int(xpostDate) >= 2015 :
        stitle=data["result"]["results"][x]["stitle"]
        address=data["result"]["results"][x]["address"][5:8]
        longitude=data["result"]["results"][x]["longitude"]
        latitude=data["result"]["results"][x]["latitude"]
        jpg_url=data["result"]["results"][x]["file"].lower().split("jpg")[0]+"jpg"   # 裡面有兩個jpg是大寫拉，被陰了
        fullData=[stitle,address,longitude,latitude,jpg_url]
        #fullData=f'{stitle},{address},{longitude},{jpg_url}'
        with open("data.csv",mode="a+",encoding="utf-8") as file:
            file.write(",".join(fullData)+"\n")

