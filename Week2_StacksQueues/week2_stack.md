**739. Daily Temperatures**
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
題目解釋：每個元素為當天溫度，輸出為隔幾天的溫度會較今天溫度高，若之後沒有比較高的溫度則輸出0

解題方向1：先將輸出ans設為全為0的array，利用for掃一輪所有日期，stack存放尚未登記的日期index，中間while判斷此index溫度是否大於stack中最後個元素對應的溫度(stack中存放的溫度會越來越低)，若溫度較低則pop最後的元素並往下判斷，並將ans對應index的答案設為當天-判斷較低溫index
``` c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> tmp;
        vector<int> ans(temperatures.size(),0);
        
        for (int i=0; i<temperatures.size(); i++){
            while (tmp.size()!=0 && temperatures[i]>temperatures[tmp.top()]){
                ans[tmp.top()] = i - tmp.top();
                tmp.pop();
            }
            tmp.push(i); //為放入ans的index
        }return ans;
        
    }
};

```
![](https://i.imgur.com/FEq1wMS.png)

解題方向2：不用stack，利用for從後往前掃，j為後幾天溫度(一開始為隔天)，如果隔天溫度較小則將j放大，若隔天溫度較大則判斷為幾天後
``` c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans(temperatures.size(),0);
        
        for (int i=temperatures.size()-2; i>=0; i--){
            int j = i + 1; 
            while(ans[j] != 0 && temperatures[j] <= temperatures[i]){
                //j += 1; 有些會太長 time limit exceeded
                j += ans[j];
            }
            if(temperatures[i]<temperatures[j]){
                ans[i] = j-i;
            }
        }return ans;
    }    
};
```
![](https://i.imgur.com/6zsczhB.png)
