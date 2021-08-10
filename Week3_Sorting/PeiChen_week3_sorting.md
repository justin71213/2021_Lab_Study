# Leetcode

## [Leetcode 164. Maximum Gap](https://leetcode.com/problems/maximum-gap/)
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.
Example:
```
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
```
### Code_1
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        num = sorted(nums)
        maxGap = 0
        for x in range(len(num) - 1):
            maxGap = max(maxGap, num[x + 1] - num[x])
        return maxGap
```
![image](https://user-images.githubusercontent.com/69243911/128641027-07a8f55b-9d64-40df-b2f1-383fe7c89291.png)

### Code_2(bucketsort)
[別人作法](https://ithelp.ithome.com.tw/articles/10201707)
* 準備桶子(最簡單的想法:設定最高值+1)
* 分類成績(將成績一一讀取，並丟到相對應的桶子，有幾個就加幾個)
* 讀取成績(依序讀取桶子裡的資料，當桶子的資料不為 0 的時候，表示在裡面有存放數字，接著將編號存回 data 裡面，看有幾個就存幾個)
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def bucketsort(data):
            s = max(nums)
            max_score = s
            bucket = []
    
            for i in range(max_score+1):
                bucket.append(0)
            for score in data:
                bucket[score] = bucket[score] + 1

            index = 0
            for i in range(len(bucket)):
                if bucket[i] != 0:
                    for j in range(bucket[i]):
                        data[index] = i
                        index += 1
        
        bucketsort(nums)        
        maxGap = 0
        for x in range(len(nums) - 1):
            maxGap = max(maxGap, nums[x + 1] - nums[x])
        return maxGap
```
![image](https://user-images.githubusercontent.com/69243911/128853169-33167ec7-9e60-47d7-85f8-768f0fd95cc1.png)

### Code_3(Radix Sort)
[別人作法](https://stackabuse.com/radix-sort-in-python)
![image](https://user-images.githubusercontent.com/69243911/128853907-1e9040df-3e9d-4bb2-8d11-4ea3537680bb.png)
![image](https://user-images.githubusercontent.com/69243911/128853799-393fcfcc-5065-4dbb-a17e-2a7e22373375.png)
![image](https://user-images.githubusercontent.com/69243911/128853867-e7444aa9-68e5-463d-9af2-1b2589b4f6b7.png)
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def countingSort(inputArray):
            # Find the maximum element in the inputArray
            maxEl = max(inputArray)

            countArrayLength = maxEl+1

            # Initialize the countArray with (max+1) zeros
            countArray = [0] * countArrayLength

            # Step 1 -> Traverse the inputArray and increase 
            # the corresponding count for every element by 1
            for el in inputArray: 
                countArray[el] += 1

            # Step 2 -> For each element in the countArray, 
            # sum up its value with the value of the previous 
            # element, and then store that value 
            # as the value of the current element
            for i in range(1, countArrayLength):
                countArray[i] += countArray[i-1] 

            # Step 3 -> Calculate element position
            # based on the countArray values
            outputArray = [0] * len(inputArray)
            i = len(inputArray) - 1
            while i >= 0:
                currentEl = inputArray[i]
                countArray[currentEl] -= 1
                newPosition = countArray[currentEl]
                outputArray[newPosition] = currentEl
                i -= 1

            return outputArray
        
        num = countingSort(nums)        
        maxGap = 0
        for x in range(len(num) - 1):
            maxGap = max(maxGap, num[x + 1] - num[x])
        return maxGap
```
![image](https://user-images.githubusercontent.com/69243911/128853169-33167ec7-9e60-47d7-85f8-768f0fd95cc1.png)
### Code_4
[別人作法](https://zhuanlan.zhihu.com/p/55000334)
* 我們首先獲取數組的最小值mixnum和最大值maxnum，得到數組的範圍.
* n個數有n-1個間隔，我們計算平均間隔gap：(maxnum-minnum)/n-1 向上取整.
* 我們計算需要的桶的個數size = int((maxnum-minnum)/gap)+1個
* 此題目的關鍵思想是：在一個桶內的數字之間的差值一定小於gap，如果某兩個數之間的差大於平均差gap，一定會被放到兩個桶內。最大的差一定大於等於gap（對一組數求平均值，平均值小於等於最大值），於是如果出現了兩個數a，b，且a和b的差大於gap，那麼a和b一定會被放到兩個連續的桶t1，t2內，且a是t1桶的嘴後一個值（最大值），b是t2桶的第一個值（最小值）。於是我們只需要記錄每個桶內的最大值和最小值，讓後用當前桶內的最小值減去上一個桶內的最大值得到maxgap，取maxgap最大的一個返回即可.
* 要注意的是，如果在計算平均距離gap時候如果得到了0，說明所有的數相等，這時可以直接返回0.
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # 有多少數字
        count = len(nums)
        # 小於兩個數字，答案為零
        if count < 2:
            return 0
        # 確定範圍，找最大最小值
        maxnum, minnum = max(nums), min(nums)
        # 計算數與數平均差距
        #（Ex:有10個數，平均差距=(max-min)/9)
        gap = math.ceil((maxnum - minnum) / (count - 1))
        # 所有數相等
        if gap == 0:
            return 0
        # 計算需要多少桶
        size = int((maxnum - minnum) / gap) + 1
        # 存储每个桶的最小值，最大值
        bucketmin, bucketmax = [sys.maxsize] * size, [-sys.maxsize] * size
        for i in range(count):
            # 计算当前值应该放到哪个桶内
            index = int((nums[i] - minnum) / gap)
            # 放最小值
            bucketmin[index] = min(bucketmin[index], nums[i])
            # 放最大值
            bucketmax[index] = max(bucketmax[index], nums[i])
        premax, maxgap = bucketmax[0], 0
        # 最大的差值为当前桶的最小值减去前一个桶的最大值
        for i in range(1, size):
            if bucketmin[i] != sys.maxsize:
                maxgap = max(maxgap, bucketmin[i] - premax)
                premax = bucketmax[i]
        return maxgap
```
![image](https://user-images.githubusercontent.com/69243911/128857199-afdf8299-a761-4917-9194-0cfa02a2f403.png)
