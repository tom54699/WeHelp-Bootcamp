import urllib.request as req
import bs4
import unicodedata
from opencc import OpenCC
import concurrent.futures
import time

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
            novellist = response.read().decode("gbk","ignore")
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
    def get_novel(self,chapterHref,i):
        request = req.Request(chapterHref,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34",
            "Accept-Language": "zh-TW"
        })
        with req.urlopen(request) as response:
            novel_text = response.read().decode("gbk","ignore")
        novel_text = novel_text.replace("<br />"," \n")
        root = bs4.BeautifulSoup(novel_text,"html.parser")
        texts = root.find_all("div",class_="uu_cont")

        for text in texts:
            content = text.get_text()
            self.novelContent[i] = f"{content}" 
            return content
    def writer(self,path,name='', content=''):
        with open(path,"a+",encoding="utf-8") as file:
            cc = OpenCC('s2t')
            file.write(cc.convert(name))
            file.writelines(cc.convert(content))
            file.write('\r\n')
           
target = input("輸入小說首頁網址:")
file_name = input("輸入檔案名稱:")
d1 = downloader(target)
d1.get_novellist()
d1.get_novel(d1.chapterHrefs[0],1)


"""
for i in range(d1.chapterNum):  
    try:
        d1.writer("text1.txt",d1.chapterNames[i],d1.get_novel(d1.chapterHrefs[i]))
    except Exception:
        print('下載出錯，已跳過')
print('下載完成')
"""
#.................................................
urls = [i for i in range(d1.chapterNum)]
def download(i):
    #d1.writer(f"絕對一番{i}.txt",d1.chapterNames[i],d1.get_novel(d1.chapterHrefs[i]))
    #d1.writer(f"絕對一番.txt",d1.chapterNames[i],d1.get_novel(d1.chapterHrefs[i]))
    d1.get_novel(d1.chapterHrefs[i],i)
start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=35) as executor:
    executor.map(download, urls)


for i in range(d1.chapterNum):
    d1.writer(f"{file_name}.txt",d1.chapterNames[d1.chapterNum-1-i],d1.novelContent[d1.chapterNum-1-i])


end_time = time.time()

print(f"{end_time - start_time} 秒爬取 {d1.chapterNum} 頁的小說")
print('下載完成')