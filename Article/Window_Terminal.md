# Window Terminal 下載安裝並更換背景圖片  
## 前言  
---
為了更像一個工程師，所以第一次使用終端機來操作MySQL。整次使用下來發現原生的Terminal很陽春，但是我不相信各位神人大大都用這個原生終端機。  
所以我就上網找到了，微軟有出一個Window Terminal，不僅可以開分頁，裡面的powershell也讓我們可以安裝不同的模組來強化使用體驗。  
這次本篇教學是以新手取向，用最簡單快速的步驟安裝好Window Terminal並更換背景圖，如果要更加深入歡迎搜尋網路上大神的分享~
## 一，打開Window 內建的 Microsoft Store  
![image](https://user-images.githubusercontent.com/108926305/196578278-c91deea6-1615-4165-b908-32ff29cd3406.png)  


直接安裝即可，完成後打開，可以試看看分頁的功能。  
<br/>
![image](https://user-images.githubusercontent.com/108926305/196578886-d3c26322-4550-4e94-a97c-09dc1f3c30b7.png)  

點擊設定裡面有些設定可以自己玩看看，可以修改配色，字體，未來有機會在分享這方面的詳細設定  
<br/>
![image](https://user-images.githubusercontent.com/108926305/196579084-edd751dd-a84b-4296-b258-80053643b115.png)

## 二、重頭戲，更換背景圖片  
> 這邊有兩種方法可以更換圖片，最簡單的是在外觀設定修改   

![外觀](https://user-images.githubusercontent.com/108926305/196583265-6f4655c4-a003-4cfb-9959-b384dbd423c6.jpg)
![背景影像](https://user-images.githubusercontent.com/108926305/196583397-3ab212c6-3220-4c2a-907f-fab31dc662ee.jpg)  

記得背景透明度要調整，圖片位置也可以唷~
<br/>  
> 另一種方法是點開啟JSON檔案，這邊建議使用VS-CODE開啟，方便做修改。   

![打開JSON](https://user-images.githubusercontent.com/108926305/196581438-7fa562e8-e1c7-47cf-a44d-2b3aba4435ae.jpg)  

打開可以發現檔名是setting.json，找到有一個name是PowerShell的那一個大括弧，把圖片中那兩行新增上去  

![背景設定](https://user-images.githubusercontent.com/108926305/196581634-d73bc51c-3bc2-4098-a890-70796f8b7745.jpg)  
```
"backgroundImage": "C:\\IMG\\Yor.png", // 放你自己的圖片路徑
"backgroundImageOpacity": 0.5,  // 透明度
```  
還有其他更細緻的設定，大家可以自己研究看看~  
- - -
最後分享我的改造成果，不只修改背景圖，有機會未來在分享其他的模組改造~  

![成品](https://user-images.githubusercontent.com/108926305/196583906-bafe123a-1109-42b9-acf3-a6656c53ac83.jpg)






