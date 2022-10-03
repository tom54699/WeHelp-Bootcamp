for i in range(5):
    print("* "*5)

for i in range(1,6):
    print("  "*(5-i),"* "*i)

for i in range(1,6):
    print("* "*i,"  "*(5-i))

for i in range(5):
    print("* "*8)

for i in range(1,6):
    print("  "*(5-i),"* "*i)

for i in range(1,6):
    print("  "*(9-(i+3)),"* "*(i+4))

for i in range(1,6):
    print("  "*(5-i)," *"*i,"* "*(i-1),"  "*(5-i))


count=0
for a in range(2,101):
    for x in range(2,a):
        if a%x==0:
            count+=1
    if count==0:
        print(a,"是質數")
    count=0


a=int(input("請輸入數字:"))
result=0
num=int(2)
for x in range(a):
    print(num)
    result+=num
    print(x)
    num=2*(10**(x+1))
print("結果",result)

a = int(input("請輸入"))
b= int(input("請輸入"))

result=0
for i in range(1,b+1):
    result=result+a*(10**(i-1))
print(result)