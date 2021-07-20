# Greatest Sum Divisible by Three

## 解題邏輯
1. 建立mod 3 = 1 and mod 3 = 2 的陣列 int one[2] , int two[2]
2. 把每個number 依照mod 3 = 1 及 mod 3 = 2 分類至 one,two陣列中，讓one,two陣列裡始終保持最小的兩個number
3. 把每個number加起來，分類
     1. 3的倍數：則總和即為答案。
     2. 3的倍數+1：要扣除一個餘1的或兩個餘2的
     3. 3的倍數+2：要扣除兩個餘1的或一個餘2的

## 程式碼
``` c
int maxSumDivThree(int* nums, int numsSize){
    int wholeSum = 0,result = 0;
    int one[2] = {10000,10000};
    int two[2] = {10000,10000};
    int temp1,temp2;
    int min_two;
    for(int i=0;i<numsSize;i++){
        int num = *(nums+i);
        wholeSum += num;
        if(num % 3 == 1){
            if(num < one[0] || num < one[1]){
                if(one[0] < one[1]){
                    one[1] = num;
                }else{
                    one[0] = num;
                }
            }
        }
        else if(num % 3 == 2){
            if(num < two[0] || num < two[1]){
                if(two[0] < two[1]){
                    two[1] = num;
                }else{
                    two[0] = num;
                }
            }
        }
    }
    switch(wholeSum % 3){
        case 0:
            result = wholeSum;
            break;
        case 1:
            
            temp2 = two[0] + two[1];
            if(one[0]<one[1]){
                temp1 = one[0];
            }
            else{
                temp1 = one[1];
            }
            if(temp1 < temp2){
                result = wholeSum - temp1;
            }
            else{
                result = wholeSum - temp2;
            }
            break;
        case 2:
            min_two = two[0]<two[1] ? two[0] : two[1];
            if(one[0]+one[1] > min_two){
                result = wholeSum - min_two;
            }
            else{
                result = wholeSum - one[0] - one[1];
            }
            break;
    }
    return result;
}
```
## 結果
