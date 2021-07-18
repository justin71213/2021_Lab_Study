# Problem 2:Two Sum
## 題目敘述
輸入一個數字的陣列**nums**及目標數字**target**，回傳該陣列中可加出目標數字的索引(index)，而且同個位置的數字不可以使用兩次，例如
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
## 解題邏輯
利用迴圈取得陣列中的每個值，在迴圈中取得第一個數字，將目標數字減去第一個數字後就可以得到第二個數字，隨後建立第二層迴圈再次檢查陣列中是否有第二個數字的值，在尋找第二個數字時如果遇到第一個數字就跳過，如果找到的話就將第一個數字及第二個數字的索引回傳。
此解法為暴力解，雖然可行但效能不是很理想。

## 程式碼
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){

    
    int i = 0;
    int j = 0;
    int pre = 0;
    int tmp = 0;
    int* returnValue;
    returnValue = (int*)malloc(numsSize * sizeof(int));
    for(i = 0;i < numsSize ;i++){
        tmp = target - nums[i]; 
        for(j = 0;j<numsSize;j++){
            if(j==i){continue;}
            else if(j == pre){continue;}
            if(nums[j]==tmp){
                returnValue[0] = i;
                returnValue[1] = j;
            }
        }
        pre = i;
    }
    *returnSize = 2;
    return returnValue;
}
```
**使用資源**:<br>
[新人做leetcode 注意这句话The returned array must be malloced, assume caller calls free().](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/solution/xin-ren-zuo-leetcode-zhu-yi-zhe-ju-hua-the-returne/)
<br>
[C 語言動態記憶體配置教學](https://blog.gtwang.org/programming/c-memory-functions-malloc-free/)

## 執行結果
![](https://github.com/justin71213/2021_Lab_Study/blob/JhihCheng/Week0/WarmUp_Ex2/JhihCheng_2/JhihCheng_2_result.jpg)