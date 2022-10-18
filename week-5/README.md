>要求二  
>創立 Member 資料表
```
CREATE TABLE member (id bigint PRIMARY KEY AUTO_INCREMENT COMMENT"獨立編號" ,name varchar(255) not null COMMENT"姓名",username varchar(255) not null Comment"帳戶名稱",password varchar(255) not null comment"帳戶密碼",follower_count int unsigned not null default 0 comment"追蹤者數量",time datetime not null default current_timestamp comment"註冊時間");
```
![image](https://user-images.githubusercontent.com/108926305/196067176-eccb7c75-9635-4023-bee7-a2479a7b6ce8.png)
- - -
>要求三  
>SQL CRUD  
>
● 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。   
 
```
INSERT INTO member(name,username,password,follower_count)VALUES("Tom","test","test",999),("Jack","jack01","123",24),("Cathy","cathy0598","456",56),("Robin","robin6891","789",35),("Seil","seil999","0000",101);
```
>指令成功畫面  

![image](https://user-images.githubusercontent.com/108926305/196068247-84be5bfe-a394-480d-a731-c60f8742fad9.png)
- - -
● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。  
```
SELECT*FROM member;
```
>確定資料輸入表格  

![image](https://user-images.githubusercontent.com/108926305/196068485-3ebf45e2-4ae1-40d8-97c5-1fe1c359cdf9.png)
- - -
● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。(這邊我又新增了幾位)  
```
SELECT*FROM member ORDER BY time DESC;
```
>排序成功  

![image](https://user-images.githubusercontent.com/108926305/196069477-f894919a-a28c-4f16-a9ff-346d7361d338.png)
- - -
● 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。  
```
SELECT*FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
>前後比對(撈出2~4 三筆資料)   
 
![image](https://user-images.githubusercontent.com/108926305/196070186-be393e76-1251-4c4e-b804-71d2d74d4a7e.png)
- - -
● 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。  
● 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。  

```
SELECT*FROM member WHERE username = "test";
SELECT*FROM member WHERE username = "test" and password = "test";
```
>兩個指令都會選到Tom  

![image](https://user-images.githubusercontent.com/108926305/196070523-b6e7caf6-0403-47bc-82e5-128025bc393a.png)
- - -
● 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。  
```
UPDATE member SET name = "test2" WHERE username = "test";
```  
>更新欄位name，並在把欄位username 是 test 的會員資料印出來  

![image](https://user-images.githubusercontent.com/108926305/196070910-506b964c-51da-45f1-a1c7-5fc3d2507391.png)
- - -  
>要求四：SQL Aggregate Functions  
>利⽤要求⼆建立的資料庫和資料表，寫出能夠滿⾜以下要求的 SQL 指令：   
 
● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
SELECT COUNT(*) AS 總共有幾個會員 FROM member;
```  
>取出有幾個會員的資料  
![image](https://user-images.githubusercontent.com/108926305/196071469-0b0ff1b9-03c2-4819-b730-9fb1873bf1cc.png)
- - -
● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。  
```
SELECT SUM(follower_count) AS 會員的粉絲總數 FROM member;
SELECT AVG(follower_count) AS 會員的平均粉絲數 FROM member;
```  
>會員的粉絲總數+平均粉絲數 (數字有點高，但是其實算低，七龍珠人氣一定更高啊!!!!)  
![image](https://user-images.githubusercontent.com/108926305/196071973-793c928b-8b22-44af-b1db-288aa0d773f3.png)
- - -
>要求五：SQL JOIN (Optional)  
● 建立一個新的"message"資料表  
```
CREATE TABLE message (id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT"獨立編號" ,member_id BIGINT NOT NULL COMMENT"留言者會員標號",content VARCHAR(255) NOT NULL COMMENT"留言內容",like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT"按讚數量",time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT"留言時間",FOREIGN KEY(member_id) REFERENCES member(id));
```  
>把"message"資料表印出來看看  
![image](https://user-images.githubusercontent.com/108926305/196073737-7401446e-61e4-4848-b25f-6e31354f40f2.png)
- - -
● 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。  
我先新增一些留言進去  
```
INSERT INTO message(member_id,content,like_count)VALUES(1,"作業快完成了",99);
INSERT INTO message(member_id,content,like_count)VALUES(1,"等一下要吃午餐",20),(1,"我就是作者拉!",9);
INSERT INTO message(member_id,content,like_count)VALUES(6,"我要毀滅世界",1),(7,"超級賽亞人變身!!!",99999),(8,"魔貫光殺炮",6666);
```
![image](https://user-images.githubusercontent.com/108926305/196074920-d1887992-6ae8-4f4a-9063-14216dcf599a.png)
> 我用inner join ，並且選擇特定要的欄位
```
SELECT member.name,message.member_id,message.content,message.like_count from member INNER JOIN message ON member.id = message.member_id;
```  
![image](https://user-images.githubusercontent.com/108926305/196080946-06aca1b8-c20c-40c3-a3a2-077686f73b74.png)
- - -  
●  使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。  

```
SELECT member.name,message.member_id,message.content,message.like_count from member INNER JOIN message ON member.id = message.member_id WHERE username = "test";
```  
>只選擇username 是 test的欄位  
![image](https://user-images.githubusercontent.com/108926305/196081397-716381dc-41ef-4d23-a274-ece78532d246.png)
- - -  
● 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。  
```
SELECT member.name,message.member_id, AVG(message.like_count) AS 所有留言平均按讚數 FROM member INNER JOIN message ON member.id = message.member_id WHERE username = "test";
```
>平均留言按讚數，這邊在CMD指令一直出錯，後來發現留言的言不知道為甚麼變成亂碼，改掉仔打一次就好了  
![image](https://user-images.githubusercontent.com/108926305/196083632-58abc836-6878-48e7-bea4-34575e081493.png)
- - -
作業完成，謝謝老師看完，很長一串。

>**額外要求**  
>我們不只要記錄留言按讚的數量，還要紀錄每一個留言的按讚會員是誰，支援以下使用場合：  
- 可以根據留言編號取得該留言有哪些會員按讚。  
- 會員若是嘗試對留言按讚：要能先檢查是否曾經按過讚，然後才將按讚的數量 +1 並且記錄按讚的會員是誰。  

剛好有看到多對多的概念(還要精進)，所以知道有 intermediary table 這個概念，所以我也創了一個 table，來放 content_id 和 like_member_id。  
> website資料庫現在有的總資料表  
> ![image](https://user-images.githubusercontent.com/108926305/196335363-858ab88a-0d4a-41da-9adf-8d81eeae72e9.png)  
> 我新增了一些貼文的按讚會員的數據進去 post_like 資料表，這邊單純紀錄文章id和對應的按讚會員標號。  
> 印出 post_like table  
> ![image](https://user-images.githubusercontent.com/108926305/196335654-6bb9385a-4d8b-4553-b38a-c8436281783f.png)  
> 那我這邊開始設想 "根據留言編號取得該留言有哪些會員按讚"，我可以用inner join來做查詢。  
> 這邊可以確定我取得了按讚會員的編號
> ![image](https://user-images.githubusercontent.com/108926305/196335869-5d7f0688-72c6-47b9-8b10-3ff6e5d02049.png)  
- - -
> 至於第二項"會員若是嘗試對留言按讚：要能先檢查是否曾經按過讚，然後才將按讚的數量 +1 並且記錄按讚的會員是誰。"  
> 根據資料庫設計，我可以在會員嘗試按讚時，先去比對資料庫中這篇文章的按讚like_member_id，如果已經存在代表按過了。  
> 如果沒按過就新增到資料庫，代表他按過了  
- - -  
這邊我再把三個資料庫的聯繫分為兩個版本印出來，一個是會員導向，一個是文章導向  
>會員導向(主要是觀察會員對哪篇文章按過讚)
```
SELECT post_like.like_member_id,member.name,post_like.content_id,message.content FROM message INNER JOIN post_like ON message.id = post_like.content_id INNER JOIN member ON member.id = post_like.like_member_id;
```  
![image](https://user-images.githubusercontent.com/108926305/196336908-6d06951f-02de-4e4a-ac33-9187678f4515.png)  
>文章導向(主要是觀察文章被誰按過讚)  
```
SELECT post_like.content_id,message.content,post_like.like_member_id,member.name FROM member INNER JOIN post_like ON member.id = post_like.like_member_id INNER JOIN message ON message.id = post_like.content_id ORDER BY content_id ASC;
```  
![image](https://user-images.githubusercontent.com/108926305/196338408-57573509-78a1-44b9-bbbb-3631b665743b.png)  
- - -
- 查詢特定會員按過誰讚  
- 查詢特定文章誰按過讚  
![image](https://user-images.githubusercontent.com/108926305/196338769-11310b10-5b66-46eb-99fa-6e8eeccb931a.png)















  


