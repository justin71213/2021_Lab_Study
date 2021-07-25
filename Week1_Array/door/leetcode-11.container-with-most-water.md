# [LeetCode 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Solution
Brute force
```c++
class Solution {
public:
    int maxArea(vector<int>& height)
    {
        int max_area = 0;
        for (int i = 0; i < height.size() - 1; i++) {
            for (int j = i + 1; j < height.size(); j++) {
                if (height[j] > height[i])
                    max_area = max(max_area, height[i] * (j - i));
                else
                    max_area = max(max_area, height[j] * (j - i));
            }
        }
        return max;
    }
};
```
![](https://i.imgur.com/HCTe6sF.png)

Optimized
```c++
class Solution {
public:
    int maxArea(vector<int>& height)
    {
        int max_area = 0, l = 0, r = height.size() - 1;

        while (l < r)
            max_area = height[l] < height[r] ? max(max_area, height[l] * (r - l++)) : max(max_area, height[r] * (r-- - l));

        return max_area;
    }
};
```
![](https://i.imgur.com/GV0BT3d.png)