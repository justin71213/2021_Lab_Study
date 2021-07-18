# twosum

## 解題邏輯
從輸入陣列的第一個元素開始，找第二個至最後一個元素中，符合加起來為target的元素。接著換第二個元素，找第三個至最後一個元素中，符合加起來為target的元素。
## 程式碼
``` c
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* ans;
    ans = (int*) malloc(numsSize * sizeof(int));
    ans[0] = 0;
    ans[1] = 1;
    
    for(int i = 0 ; i< numsSize-1 ; i++){
        int b = target - *(nums + i);  
        for(int j=i+1 ; j<numsSize ; j++){
            if (*(nums + j) == b){
                ans[0] = i;
                ans[1] = j;
                break;
            }
        }
        
    }
   *returnSize = 2;
    return ans;
}
```
## 結果
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week0/WarmUp_Ex2/XiangWei_2/XiangWei_2.png)
