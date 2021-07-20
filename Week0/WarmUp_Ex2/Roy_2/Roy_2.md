* Two Sum
```python=
 class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #遍歷每個數字
        for num in nums:
            #如果第一個數小於target
            if num<target:
                index = nums.index(num)
                #如果後面有數字跟第一個數字相加等於target
                if target-num in nums[index+1:]:
                    index2 = nums[index+1:].index(target-num)+(index+1)
                    break
        return [index,index2]
```
![](https://i.imgur.com/IzN4uHk.png)