"""
要求一：函式與流程控制
完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可
以假設 max 一定大於 min 且為整數，step 為正整數。

"""
def calculate(min, max, step):
    # 請用你的程式補完這個函式的區塊
    if (max>min)and(step>0):
        number=0
        for x in range(min,max+1,step):
            number+=x
        print(number)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0
# 用range(start,stop,step)
"""
要求二：Python 字典與列表、JavaScript 物件與陣列
完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
不定的情況。

"""
def avg(data):
# 請用你的程式補完這個函式的區塊
    salary=0
    avgnum=0
    for x in data["employees"]:
        if(x["manager"]==False):
            salary+=x["salary"]
            avgnum+=1
    avg=salary/avgnum
    print(avg)
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

"""
要求三：
完成以下函式，最後能印出程式中註解所描述的結果。

"""
def func(a):
    def count(c,d):
        print(a+(c*d))
    return count

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
# 如果看見括弧后還有一個括弧，說明第一個函數返回了一個函數，如果後面還有括號，說明前面那個也返回了一個函數。 以此類推。

"""
要求四：
找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

"""
def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    a=[]
    b=[]
    a = [x for x in nums if x>=0]
    b = [x for x in nums if x<0]

    # 如果只有一個正數，負數，沒得選
    if (len(a)<2 and len(b)<2 ):
        max_value = max(nums)
        del nums[nums.index(max_value)]
        secondmax_value = max(nums)
        ans=max_value*secondmax_value
        print(ans)
    # 如果只有一個正數，那就負數絕對值後挑兩個最大的互乘
    elif(len(a)<2):
        absList = list(map(abs, b)) # 絕對值
        max_value = max(absList)
        del absList[absList.index(max_value)]
        secondmax_value = max(absList)
        ans=max_value*secondmax_value
        print(ans)
    # 如果只有一個負數，那就正數選兩個最大的互乘
    elif(len(b)<2):
        max_value = max(nums)
        del nums[nums.index(max_value)]
        secondmax_value = max(nums)
        ans=max_value*secondmax_value
        print(ans)
    # 如果正數和負數各有兩個或以上，那就正的最大的前兩個和負的絕對值後最大的兩個來比
    else:
        def multiply(num):
            absList = list(map(abs, num)) # 絕對值
            max_value = max(absList)
            del absList[absList.index(max_value)]
            secondmax_value = max(absList)
            ans=max_value*secondmax_value
            return ans 
        c=multiply(a)
        d=multiply(b)
        if (c>d):
            print(c)
        else:
            print(d)  
"""
    max_value = max(nums)
    del nums[nums.index(max_value)]
    secondmax_value = max(nums)
    ans=max_value*secondmax_value
    print(ans)
"""
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

"""
要求五：
Given an array of integers, show indices of the two numbers such that they add up to a
specific target. You can assume that each input would have exactly one solution, and you
can not use the same element twice.

"""

def twoSum(nums, target):
    result=[]
    for x in range(len(nums)):
        for i in range(len(nums)):
            if nums[x]+nums[i]==target:
                result+=[x]
                result+=[i]  
                return result 
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

"""
要求六 ( Optional )：
給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
長度。

"""
def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    result=0
    num=[]
    for x in nums:
        if x == 0:
            result+=1
            num+=[result]
        else:
            result=0
            num+=[result]
    print(max(num))
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
