### Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

![](https://i.imgur.com/emLzqP6.png)

**解題邏輯**
* 從外往內判斷
* 以較短的柱子判斷下一根柱子要不要計算 或 兩根柱子相遇
* 若下一根柱子比短的柱子長再判斷容量
* 
``` c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int front = 0;
        int end = height.size()-1;
        int contain = 0;
        int low;
        
        while (front < end){
            low = min(height[front], height[end]);
            contain = max(contain, low*(end-front));
            
            if (height[front] <= height[end]){                
                while (height[++front] < low && front < end);
            }
            
            else{               
                while (height[--end] < low && front < end);
            }
        }return contain;
    }
};
```
![](https://i.imgur.com/IXANoUg.png)
