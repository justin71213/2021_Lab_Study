# [Problem 46.Permutations](https://leetcode.com/problems/permutations/)
## 題目敘述
輸入一串不重複的數字的陣列，列出包含所有的排列組合的二維陣列
例如:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
## 解題邏輯
每多一個新元素的排列組合就是將新元素安插在舊的排列組合的間隔，例如:<br>
[ 1 , 2 ]的排列組合->2插入[ 1 ] -> [ _ , 1 ]or [ 1 , _ ]<br>
使用遞迴取得舊的排列組合
## 程式碼(Python3)
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        #到最底層返回
        if len(nums) == 1:
            return [nums]
        else:
            #把第一個元素當新元素，剩下的傳入遞迴作舊的排列組合
            tmp = self.permute(nums[1:].copy())
            for sub in tmp:
                #輪流插入不同位置
                for i in range(len(sub)+1):
                    temp2 = sub.copy()+[0]
                    temp2.insert(i,nums[0])
                    temp2.pop()
                    #將不同位置的結果記錄下來
                    res.append(temp2)
        return res
```
## 結果
```
Success
Details 
Runtime: 36 ms, faster than 89.19% of Python3 online submissions for Permutations.
Memory Usage: 14.2 MB, less than 89.06% of Python3 online submissions for Permutations.
```

## 另解(C)
```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#define LEN 0xffff

void swap(int*a, int*b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void rec(int *arr, int len, int index, int **ret, int *ret_index){
    int i;
    if(index == len-1)
    {
        ret[*ret_index] = (int *)malloc(sizeof(int) * len);
        memcpy(ret[*ret_index], arr, len*sizeof(int));
        (*ret_index)++;
        return;
    }

    for(i=index; i<len; i++)
    {
        swap(&arr[i], &arr[index]);
        rec(arr, len, index+1, ret, ret_index);
        swap(&arr[i], &arr[index]);
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
    //二維陣列
    int **ret = (int **)malloc(sizeof(int*)*LEN); 
    //每行長度 
    int *retSize = (int *)malloc(sizeof(int)*LEN); 
    //行數
    int retIndex = 0;     
    int i = 0;

    rec(nums, numsSize, 0, ret, &retIndex);                          
    *returnColumnSizes = retSize;
    for(i = 0; i<retIndex;i++)
    {
        retSize[i] = numsSize;
    }

    *returnSize = retIndex; //行數

    return ret;
}
```

## 另解結果
```
Success
Details 
Runtime: 12 ms, faster than 57.04% of C online submissions for Permutations.
Memory Usage: 10 MB, less than 18.52% of C online submissions for Permutations.
```

## 參考資源
[LeetCode:46. Permutations 全排列(C语言)](https://blog.csdn.net/wangqingchuan92/article/details/104145290)