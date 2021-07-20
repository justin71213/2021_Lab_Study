# EX1. Greatest Sum Divisible by Three

## Intro

[1262. Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)

## Method

[Soruce](https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space)

Add new list `dp2 = dp.copy()` to fix bug.

```python
def maxSumDivThree(nums: list) -> int:
    """
    DP[0]: Maximum value that divisible by 3.
    DP[1]: Maximum value that divided by 3 with remainder 1.
    DP[2]: Maximum value that divided by 3 with remainder 2.
    """
    dp = [0, 0, 0]
    for num in nums:
        dp2 = dp.copy()  # <--- add this line
        for i in dp2:  # 3 cases. (Change dp to dp2.)
            dp[(num + i) % 3] = max(dp[(num + i) % 3], num + i)
    return dp[0]
```
