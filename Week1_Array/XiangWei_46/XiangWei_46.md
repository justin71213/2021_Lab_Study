# 46. Permutations
## discription
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

## flow
以排列ABC為例：
1. A開頭，排列BC
    - B開頭，排列C
    - C開頭，排列B
2. B開頭，排列AC
    - A開頭，排列C
    - C開頭，排列A
3. C開頭，排列AB
    - B開頭，排列A
    - A開頭，排列B
  
