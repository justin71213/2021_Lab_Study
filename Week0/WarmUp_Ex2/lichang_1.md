# EX2. Two Sum

## Intro

[1. Two Sum](https://leetcode.com/problems/two-sum/)

## Method 1:

**Brute-force search:** 使用雙層 for 迴圈尋找符合 target 的元素。

**code:**

```python
def twoSum(self, nums: int, target: int):
    """
    1. assume that each input would have exactly one solution
    2. you may not use the same element twice.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

## Method 2:

[Source](https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time)

**code:**

```python
def twoSum(self, nums: int, target: int):
    goal = {}
    for idx, num in enumerate(nums):
        remaining = target - num
        if num in goal:
            return [goal[num], idx]
        else:
            goal[remaining] = idx
```
