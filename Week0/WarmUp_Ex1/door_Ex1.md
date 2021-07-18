# [Leetcode 1262. Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
Example:
```
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
```
Maintain the maximum of `mod 3 == 0`,  `mod 3 == 1` and `mod 3 == 2`
```
Take 3
{ 3 0 0 }
Take 6
{ 9 0 0 }
Take 5
{ 9 0 14 }
Take 1
{ 15 10 14 }
Take 8
{ 18 22 23 }

Result: 18
```
## Code
```cpp
class Solution {
public:
    int maxSumDivThree(vector<int>& nums)
    {
        int k[2][3] = { { 0, 0, 0 }, { 0, 0, 0 } };
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < 3; j++) {
                int temp = k[0][j] + nums[i];
                k[1][temp % 3] = max(k[1][temp % 3], temp);
            }
            for (int j = 0; j < 3; j++) {
                k[0][j] = k[1][j];
            }
        }
        return k[0][0];
    }
};
```
![](https://i.imgur.com/rGninFd.png)