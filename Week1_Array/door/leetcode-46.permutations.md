# [Leetcode 46. Permutations](https://leetcode.com/problems/permutations/)

## Solution
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums)==1:
            return [nums]
        for num in nums:
            temp = nums[:]
            temp.remove(num)
            for sublist in self.permute(temp):
                res.append([num]+sublist)
        return res
```