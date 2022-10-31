import urllib.request as req
import bs4
import unicodedata
from opencc import OpenCC
import concurrent.futures
import time
import asyncio
import aiofiles
import aiohttp
import unicodedata

# 小說下載器
class downloader():
    # 初始化
    def __init__(self,target):
        self.target = target
        self.novelContent = {}
        self.chapterNames = []
        self.chapterHrefs = []
        self.chapterNum = 0
    # 拿章節
    def get_novellist(self):
        request=req.Request(self.target,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34",
            "Accept-Language": "zh-TW"
        })
        with req.urlopen(request) as response:
            novellist = response.read().decode("utf-8","ignore")
        # print(novellist) 完整的html

        root = bs4.BeautifulSoup(novellist,"html.parser")
        list = root.find("ul",id="chapterList")
        list_title = list.find_all("a")
        for title in list_title:
            Hrefs = title.get("href")
            Names = title.string
            self.chapterHrefs.append("https://www.uukanshu.com/"+Hrefs)
            self.chapterNames.append(Names)
        self.chapterNum += len(list_title)
    # 拿小說內文

    async def get_novel(self,chapterHref,i):
        headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34",
        "Accept-Language": "zh-TW"
        }
        # 遇到連線逾時可以改底下這樣
        #con = aiohttp.TCPConnector(ssl=False)
        #async with aiohttp.ClientSession(connector=con, trust_env=True) as session:
            #async with session.get(url=chapterHref) as resp:
        async with aiohttp.request("get",url=chapterHref) as resp:
            novel_text = await resp.text("gbk")
        novel_text = novel_text.replace("<br />"," \n")
        root = bs4.BeautifulSoup(novel_text,"html.parser")
        texts = root.find_all("div",class_="uu_cont")

        for text in texts:
            content = text.get_text(strip=True)
            content =unicodedata.normalize('NFKC', str(content))
            self.novelContent[i] = f"{d2.chapterNames[i]}'\n'{content}" 
            return content

    def writer(self,path, content=''):
        with open(path,"a",encoding="utf-8") as file:
            cc = OpenCC('s2t')
            #file.write(cc.convert(name))
            file.writelines(cc.convert(content))
            #file.write('\r\n')

    async def download(self,i):
        await d2.get_novel(d2.chapterHrefs[i],i)

target = input("輸入小說首頁網址:")
file_name = input("輸入檔案名稱:")
d2 = downloader(target)
d2.get_novellist()



async def main():
    start_time = time.time()
    tasks = []
    for i in range(d2.chapterNum):
        task = asyncio.create_task(d2.download(i))
        tasks.append(task)
    for task in tasks:
        await task
    end_time = time.time()
    print(f"{end_time - start_time} 秒爬取 {d2.chapterNum} 頁的小說")
    



loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())

start_time = time.time()

# 把章節都放在一起
novel_content = sorted(d2.novelContent)
novel_content =[d2.novelContent[key] for key in novel_content]

novel_content = "\n".join(novel_content)
rs = novel_content.replace("\\n", " ")


d2.writer(f"{file_name}.txt",rs)



"""
for i in range(d2.chapterNum):
    d2.writer(f"{file_name}.txt",d2.chapterNames[d2.chapterNum-1-i],d2.novelContent[d2.chapterNum-1-i])
"""

end_time = time.time()
print(f"{end_time - start_time} 秒寫入 {d2.chapterNum} 頁的小說")