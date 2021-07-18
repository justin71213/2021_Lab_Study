# Problem 1:maxSumDivThree
## 題目敘述
輸入一個數字的陣列**nums**，找出為3的倍數的最大總和，例如:
```
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
```
## 解題邏輯
不為3的倍數有兩種可能
1. 餘數為1<br>
2. 餘數為2<br>

題目要求找出最大值，所以先計算出所有數字的總和再倒扣最小的數即可達成，此時要湊出最小且餘數與總和相同的值。<br>
有兩種情況下餘數會為1:
1. 本身餘數就為1
2. 兩個餘數為2的數相加<br>
&emsp;(3m+2)+(3n+2) = 3(m+n)+4 =3k+1

同理有兩種情況下餘數會為2:
1. 本身餘數就為2
2. 兩個餘數為1的數相加<br>

所以在一開始先各自記錄餘數為1以及餘數為2最小值與第二小的值，計算出總和的餘數後取得對應餘數的最小值以及另外一邊兩個數的和並取較小的一方，減去即可滿足題目條件。

## 程式碼
```c
int maxSumDivThree(int* nums, int numsSize){
    int i;
    int oddMin = 10000;
    int secondOddMin = 10000;
    int evenMin = 9999;
    int secondEvenMin = 10000;
    int sum = 0;
    
    for(i=0;i<numsSize;i++){
        //caculate summation
        sum = sum + nums[i];
        //record minimum & second minimum of remainder is 2
        if(nums[i] %3 == 2){
            if(nums[i] <evenMin){
                secondEvenMin = evenMin;
                evenMin = nums[i];
            }
            else if(secondEvenMin > nums[i]){
                secondEvenMin = nums[i];
            }
        }
        //record minimum & second minimum of remainder is 1
        else if(nums[i] %3 == 1){
            if(nums[i] < oddMin){
                secondOddMin = oddMin;
                oddMin = nums[i];
            }
            else if(secondOddMin > nums[i]){
                secondOddMin = nums[i];
            }
        }
    }

    //caculate remainder of summation
    if(sum%3 == 2){
        //summation - min(econdOddMin+oddMin,evenMin)
        if(secondOddMin+oddMin < evenMin){
            sum = sum - secondOddMin - oddMin;
        }
        else{
            sum = sum - evenMin;
        }
    }
    else if(sum%3 == 1){
        //summation - min(secondEvenMin+evenMin,oddMin)
        if(secondEvenMin+evenMin < oddMin){
            sum = sum - secondEvenMin - evenMin;
        }
        else{
            sum = sum - oddMin;
        }
    }
    return sum;
}
```
## 執行結果
![](https://github.com/justin71213/2021_Lab_Study/blob/JhihCheng/Week0/WarmUp_Ex1/JhihCheng_1/JhihCheng_2_result.png)