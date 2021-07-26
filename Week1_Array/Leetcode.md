# Leetcode

## [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
Example:
```
Input: nums = [1,2,0]
Output: 3
```
## Code_1
逐筆檢查 
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1
```
![image](https://user-images.githubusercontent.com/69243911/127019290-4c3dc49d-cea8-4f67-97c1-58e035c7ff2a.png)

## Code_2
* 如果數組的長度是L，那麼結果最大就是L+1
* 給數組加一個0（處理0的情況），把長度令為l
* 把所有負數和大於等於l的數，都變成0
* 遍歷數組，把數對應下標的數加上l(把陣列位置當作數字是否出現過)
* (所以現在陣列內數字不重要)
* 再遍歷一遍，第一個小於l的數，他的位置i就是結果(代表那個位置沒有出現過)
* 但如果沒有小於l的數，結果就為l
![image](https://user-images.githubusercontent.com/69243911/127035902-3f8779ed-4728-4999-8042-222a28a2858c.png)

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        l = len(nums)
        if l == 1:   #代表無輸入
            return 1
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0
        for i in range(l):
            nums[nums[i] % l] += l
        for i in range(1, l):
            if nums[i] < l:
                return i
        return l
```
![image](https://user-images.githubusercontent.com/69243911/127019341-cde7cdc6-555c-4e62-a449-1e47d7e1dc5f.png)