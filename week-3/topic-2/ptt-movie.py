import urllib.request as req
import bs4


def getTitle(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="title")
    good_movie=[]
    normal_movie=[]
    bad_movie=[]
    for title in titles:
        
        if title.a !=None:
            if title.a.string[0:4]=="[好雷]":
                good_movie.append(title.a.string)
                print(good_movie)
            elif title.a.string[0:4]=="[普雷]":
                normal_movie.append(title.a.string)
            elif title.a.string[0:4]=="[負雷]":
                bad_movie.append(title.a.string)
    next_link=root.find("a", string="‹ 上頁")
    return "https://www.ptt.cc/"+next_link["href"],good_movie,normal_movie,bad_movie


pageurl="https://www.ptt.cc/bbs/movie/index.html"
url_data=[]
good_movie=[]
normal_movie=[]
bad_movie=[]
for i in range(10):
    url_data=getTitle(pageurl)
    pageurl=url_data[0]
    good_movie.extend(url_data[1])
    normal_movie.extend(url_data[2])
    bad_movie.extend(url_data[3])
movie_list="\n".join(good_movie+normal_movie+bad_movie) 

with open("movie.txt",mode="a+",encoding="utf-8") as file:
    file.write(movie_list)

