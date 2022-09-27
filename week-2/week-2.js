/* 

要求一：函式與流程控制
完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可
以假設 max 一定大於 min 且為整數，step 為正整數。

*/
function calculate(min, max, step){
    // 請用你的程式補完這個函式的區塊
    let result=0;
    if(max>min && step>0){
        for(let x=min;x<=max;x+=step){
            result+=x
        }
        console.log(result)
    }
}
calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0
// 用數學公式+Math.floor處理

/* 

要求二：Python 字典與列表、JavaScript 物件與陣列
完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
不定的情況。

*/
function avg(data){
    // 請用你的程式補完這個函式的區塊
    let salary=0;
    let avgnum=0;
    for(let x=0;x<data["employees"].length;x++){
        if(data["employees"][x]["manager"]==false){
            salary+=data["employees"][x]["salary"];
            avgnum+=1;
        }
    }
    let avg=salary/avgnum;
    console.log("平均薪資:"+avg)
}
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":false
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":true
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":false
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":false
        }
    ]
}); // 呼叫 avg 函式


/*

要求三：
完成以下函式，最後能印出程式中註解所描述的結果。

*/

function func(a){
    function count(c,d){
        console.log(a+(c*d))
    }
    return count
}
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
    // 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
/*

要求四：
找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

*/ 

function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊
    let a=[];
    let b=[];
    nums.forEach(function(x){
        if (x>=0){
            a.push(x);
        }
        if (x<0){
            b.push(x);
        } 
    });

    //如果只有一個正數，負數，沒得選
    if (a.length<2 && b.length<2 ){
        let max_value = Math.max(...nums);
        let index=nums.indexOf(max_value);
        nums.splice(index);
        let secondmax_value = Math.max(...nums);
        let ans=max_value*secondmax_value;
        console.log(ans);
    }
        
    // 如果只有一個正數，那就負數絕對值後挑兩個最大的互乘
    else if(a.length<2){
        let absList = b.map(Math.abs); // 絕對值
        let max_value = Math.max(...absList);
        let index=absList.indexOf(max_value);
        absList.splice(index,1);   //這邊splice後面沒指定1會變成全刪，很奇怪
        let secondmax_value = Math.max(...absList);
        let ans=max_value*secondmax_value;
        console.log(ans);
    }
        
    // 如果只有一個負數，那就正數選兩個最大的互乘
    else if(b.length<2){
        let max_value = Math.max(...a);
        let index=a.indexOf(max_value);
        a.splice(index,1);
        let secondmax_value = Math.max(...a);
        let ans=max_value*secondmax_value;
        console.log(ans);
    }
        
    // 如果正數和負數各有兩個或以上，那就正的最大的前兩個和負的絕對值後最大的兩個來比
    else{
        function multiply(num){
            let absList = num.map(Math.abs); // 絕對值
            let max_value = Math.max(...absList);
            let index=absList.indexOf(max_value);
            absList.splice(index,1);
            let secondmax_value = Math.max(...absList);
            let ans=max_value*secondmax_value;
            return ans 
        }
        c=multiply(a)
        d=multiply(b)
        if (c>d){
            console.log(c);
        }
        else{
            console.log(d);
        }
    }
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10
/*

要求五：
Given an array of integers, show indices of the two numbers such that they add up to a
specific target. You can assume that each input would have exactly one solution, and you
can not use the same element twice.

*/ 

function twoSum(nums, target){
    let result=[];
    for(let x=0; x<nums.length;x++){
        for(let y=0; y<nums.length;y++){
            if(nums[x]+nums[y]==target){
                result.push(x)
                result.push(y)
                return result
            }
        }
    }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

/*

要求六 ( Optional )：
給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
長度

*/ 

function maxZeros(nums){
    let result=0;
    let num=[];
    for(let x=0;x<nums.length;x++){
        if (nums[x]==0){
            result++;
            num.push(result);
        }else{
            result=0;
            num.push(result);
        }
    }
    console.log(Math.max(...num))
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3