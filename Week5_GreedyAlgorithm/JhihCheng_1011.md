# [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/)
## 題目敘述
提供一串i個貨物重量的陣列及配送天數請找出**最小的**配送上限使得貨物能在規定天數內送完<br>
**注意陣列內容不能調換順序且必須每天都有乘載貨物**<br>
例如:
```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
```
## 解題邏輯
運用二元搜尋來找出最小值，一開始下限為最重的貨物(比它小怎麼樣都沒辦法載)，上限先設為貨物總重，最後中間值為負重。<br>
透過負重來計算所花的天數，如果低於需求會使天數超過設定天數，過大則相反，如此反覆搜尋最低需求。
## 程式碼
```c
int shipWithinDays(int* weights, int weightsSize, int days){
    int max = 0;   //binary search上限
    int min = 0;   //binary search底限
    int mid = 0;
    int used_day;  //負重mid的情況下需要耗費的天數
    int daily_sum; //當天的負重
    int i;
    
    //找出上下限，下限是最重的貨物，上限先用總重
    for(i = 0;i < weightsSize;i++){
        max += weights[i];
        if(weights[i] > min)
            min = weights[i];
    }
    
    //開始binary search
    while(min < max){
        mid = (min + max) / 2;
        used_day = 0;
        daily_sum = 0;
        
        //計算不超過mid的負重下運送要花幾天
        for(i = 0;i < weightsSize;i++){
            daily_sum += weights[i];
            if(daily_sum > mid){
                daily_sum = 0;
                i--;
                used_day++;
            }
        }
        
        //修正最後一天不會被看到
        if(daily_sum > 0)
            used_day++;
        
        //天數比給定的多代表負重太少，往大的地方找，比給定的少則相反
        if(used_day > days)
            min = mid+1;
        else
            max = mid;
    }
    
    return min;
}
```
## 複雜度
時間複雜度:O(log(n)\*n)<br>
空間複雜度:O(1)
## 運行結果
Runtime: 36 ms(87.50%) ~ 40ms(62.5%)
Memory Usage: 8.4 MB(100.00%) ~ 8.8(25%)
## 資料來源
[C solution using binary search](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/335820/C-solution-using-binary-search)
[6 questions in one template of binary search - for beginners! - python](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/819127/6-questions-in-one-template-of-binary-search-for-beginners!-python)
[猩猩的乐园 Leetcode 1011 Capacity To Ship Packages Within D Days](https://www.youtube.com/watch?v=t2eQB9-EqPg)
