# [Leetcode 41. First Missing Positive](https://leetcode.com/problems/two-sum/)
Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that **runs in O(n) time** and **uses constant extra space**.

**Example 1:**
```
Input: nums = [1,2,0]
Output: 3
```
**Example 2:**
```
Input: nums = [3,4,-1,1]
Output: 2
```
**Example 3:**
```
Input: nums = [7,8,9,11,12]
Output: 1
```
**Constraints:**
- 1 <= nums.length <= 5 * 10<sup>5</sup> 
- -2 <sup>31</sup> <= nums[i] <= 2 <sup>31</sup> - 1

## Solution
First `for` loop:
- Put `1` at `nums[0]`, `2` at `nums[1]` and so on.
- These two value are invalid, make them `-1`.
    - `nums[i]` > `numsSize`
    - `nums[i]` <= `0`

Second `for` loop:
- At last, find the **first** `nums[i] == -1` and return `i+1`

`ctz` and `clz` in [GCC extension](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html)

> Built-in Function: int __builtin_ctz (unsigned int x)
> * Returns the number of trailing 0-bits in x, starting at the least significant bit position. If x is 0, the result is undefined.  
>
> Built-in Function: int __builtin_clz (unsigned int x)
> * Returns the number of leading 0-bits in x, starting at the most significant bit position. If x is 0, the result is undefined.
```c
#define SWAP(x, y) \
    int tmp = x;   \
    x = y;         \
    y = tmp;

int firstMissingPositive(int* nums, int numsSize)
{

    for (int i = 0; i < numsSize; i++) {
        int pos = nums[i] - 1;
        if (nums[i] > 0 && nums[i] <= numsSize) {
            if (pos != i && nums[i] != nums[pos]) {
                SWAP(nums[i], nums[pos]);
                i--;
            } else if (pos != i && nums[i] == nums[pos])
                nums[i] = -1;
        } else
            nums[i] = -1;
    }

    for (int i = 0; i < numsSize; i++) {
        if (!__builtin_clz(nums[i]))
            return i + 1;
    }

    return numsSize == 0 ? 1 : numsSize + 1;
}
```