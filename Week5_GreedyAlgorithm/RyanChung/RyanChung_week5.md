### 題目： [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

> A conveyor belt has packages that must be shipped from one port to another within days days.
>
> The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
>
> Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

#### Example
- Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
- Output: 15
```
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
```

#### Constraints:
- 1 <= days <= weights.length <= 5 * 10^4
- 1 <= weights[i] <= 500

---

### 原始想法（硬算）
從最重的 package weight 開始，由前往後塞滿容量，超出天數就將容量+1，然後重算。
```python
class Solution(object):
    def shipWithinDays(self, weights, days):
        
        max_weight = max(weights)
        
        while True:
            num,temp = 1,0
            for weight in weights:
                if (temp + weight) <= max_weight:
                    temp += weight
                else:
                    temp = weight
                    num += 1
                    
            if num <= days:
                break
            else:
                max_weight += 1
        
        return max_weight
```
| 空間 | 時間 |
|:----:|:----:|
| O(1) | O(n)～O( n\*Sum(n) ) <= O( n^2 \*500 ) |

Worst Case: Day = 1
```
[500,500,500,...,500]
1
```
結果：**Time Limit Exceeded**  
可以透過補丁一直改，但大家都用 Binary Search 優化問題  

### Binary Search
- 概念：將數列排序後，從中位數開始比較，去掉一半的數列，再重新比較（類似猜數字）。
- 命題：貨櫃容量從 Max(weights) ～ Sum(weights)，我們想知道某個容量。
- 判斷式：天數 <= days ?

```python
class Solution(object):
    def shipWithinDays(self, weights, days):
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            num, temp = 1, 0
            mid = (left+right)/2
            
            for weight in weights:
                if (temp + weight) <= mid:
                    temp += weight
                else:
                    temp = weight
                    num += 1
                
            if num <= days:
                right = mid
            else:
                left = mid + 1
        
        return left
```
| 空間 | 時間 |
|:----:|:----:|
| O(1) | O(n)～O( n\*logn ) |

結果：  
Runtime: 436 ms ( 76.02% )  
Memory: 15.1 MB ( 94.39% )  

### Program in C
```c
int shipWithinDays(int* weights, int weightsSize, int days){
    
    int left = 0, right = 0;
    for (int i=0; i<weightsSize; i++) {
        if (left < weights[i]) left = weights[i];
        right += weights[i];
    }
    
    while (left < right) {
        int num = 1, temp = 0;
        int mid = (left+right)/2;
            
        for (int i=0; i<weightsSize; i++) {
            if ((temp + weights[i]) <= mid)
                temp += weights[i];
            else{
                temp = weights[i];
                num += 1;
            }    
        }
        if (num <= days) right = mid;
        else left = mid + 1;
    }
    return left;
}
```
結果：  
Runtime: 40 ms ( 62.5% )  
Memory: 8.4 MB ( 100% )  

###### tags: `LeetCode`