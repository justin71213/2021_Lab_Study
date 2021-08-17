# [Leetcode 10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
## Solution
- 嘗試 [FSM](https://en.wikipedia.org/wiki/Finite-state_machine) 方法失敗
- 改用 Dynamic programing
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for j in range(len(p)+1)] for i in range(len(s)+1)]

        # "" , "" : start point
        dp[0][0] = True

        # "" , a*c*.*....
        for i in range(2 , len(p)+1, 2):
            if p[i-1] == "*":
                 dp[0][i] = True
            else:
                break

        for i in range(1 , len(s)+1):
            for j in range(1 , len(p)+1):
                if p[j-1] == "." or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])

        return dp[len(s)][len(p)]
```