# EX1. Greatest Sum Divisible by Three

## Intro

[1262. Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)

## Method

[Method soruce](https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space)

```python
def maxSumDivThree(nums: list) -> int:
    """
    DP[0]: Maximum value that divisible by 3.
    DP[1]: Maximum value that divided by 3 with remainder 1.
    DP[2]: Maximum value that divided by 3 with remainder 2.
    """
    dp = [0, 0, 0]
    for num in nums:
        for i in dp[:]:  # 3 cases. (Change dp to dp2.)
            dp[(num + i) % 3] = max(dp[(num + i) % 3], num + i)
    return dp[0]
```

## Appendix

`for i in dp[:]:` 與 `for i in dp:` 會有不同結果，
之前的上傳錯誤問題是由此差異產生。

**example:**

```python
a = [i for i in range(10)]

for i in a[:]:
    print(i)
    if i % 2 == 0:
        a.remove(i)
print(a)
print('='*20)

a = [i for i in range(10)]

for i in a:
    print(i)
    if i % 2 == 0:
        a.remove(i)
print(a)
```
