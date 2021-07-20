# Week0
* Greatest Sum Divisible by Three
```python=
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()    #nums排序
        nums_sum = sum(nums)    #計算nums的總和
        dicts = defaultdict(list)    #創建字典, 字典的value為空list
        #if總和餘數為2
        if nums_sum%3 == 2:
            #遍歷排序過的nums
            for num in nums:
                rmd = num%3    #rmd:remainder餘數
                dicts[rmd].append(num)    #餘數為字典的key  
                #當未出現2個餘數為1的數字, 且出現餘數為2的數字
                if len(dicts[1]) < 2 and len(dicts[2]) == 1 :
                    return nums_sum-dicts[2][0]
                #當出現2個餘數為1的數字時
                elif len(dicts[1]) >= 2:
                    #如果還未出現餘數為2的時候，如果餘數為1的兩個數字小於目前的num，則return
                    if dicts[2] == []:
                        if dicts[1][0]+dicts[1][1] < num :
                            return nums_sum-(dicts[1][0]+dicts[1][1])
                    #如果出現餘數為2的時候，判斷餘數為1的最小兩個數字總和是否大於餘數為2的數字
                    elif dicts[2] != []:
                        if dicts[1][0]+dicts[1][1] > dicts[2][0]:
                            return nums_sum-dicts[2][0]       
                        else:
                            return nums_sum-(dicts[1][0]+dicts[1][1])      
        elif nums_sum%3 == 1:
            for num in nums:
                rmd = num%3    #rmd:remainder餘數
                dicts[rmd].append(num)
                if len(dicts[2]) < 2 and len(dicts[1]) == 1 :
                    return nums_sum-dicts[1][0]
                elif len(dicts[2]) >= 2:
                    if dicts[1] == []:
                        if dicts[2][0]+dicts[2][1] < num :
                            return nums_sum-(dicts[2][0]+dicts[2][1])
                    elif dicts[1] != []:
                        if dicts[2][0]+dicts[2][1] > dicts[1][0]:
                            return nums_sum-dicts[1][0] 
                        else:
                            return nums_sum-(dicts[2][0]+dicts[2][1])
        else:
            return nums_sum
```
![](https://i.imgur.com/cJWwgKE.png)
