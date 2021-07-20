# Leetcode

## [Leetcode 1. Two Sum](https://leetcode.com/problems/two-sum/)

Example:
```
Input: nums = [3,6,5,1,1010], target = 7
Output: [1,3]
```
### Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2 = nums[i+1:]           #防止重複 
            for j in range(len(num2)):
                if (nums[i] + num2[j]) == target:
                    return i, j+i+1
```
![image](https://user-images.githubusercontent.com/69243911/126322610-cf6d57e0-daba-450c-922f-a64740554438.png)
