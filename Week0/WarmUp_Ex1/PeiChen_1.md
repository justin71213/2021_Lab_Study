# Leetcode

## [Leetcode 1262. Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
Example:
```
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
```
### Code
```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        #判斷內容物的性質
        a = [x for x in nums if x % 3 == 0] #三的倍數
        b = sorted([x for x in nums if x % 3 == 1], reverse=True) #除以三餘一，並反向排序
        c = sorted([x for x in nums if x % 3 == 2], reverse=True) #除以三餘二，並反向排序
        total = sum(nums)
        ans = 0
        #判斷最終答案
        if total % 3 == 0:  #總和剛好為三倍數
            ans = total
        if total % 3 == 1:
            if len(b) >= 1:     #減少一個餘數為1的內容物
                ans = max(ans, total - b[-1])
            if len(c) >= 2:     #減少兩個餘數為2的內容物
                ans = max(ans, total - sum(c[-2:]))
        elif total % 3 == 2:    
            if len(b) >= 2:     #減少兩個餘數為1的內容物
                ans = max(ans, total - sum(b[-2:]))
            if len(c) >= 1:     #減少一個餘數為2的內容物
                ans = max(ans, total - c[-1])

        return ans
```
![image](https://user-images.githubusercontent.com/69243911/126322365-9f45516c-a745-4264-b0da-49a3f2903c06.png)
