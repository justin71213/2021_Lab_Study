# Week3: Sorting

## 23. Merge k Sorted Lists

[Problem link](https://leetcode.com/problems/merge-k-sorted-lists/)

**method 1:**

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return ListNode('')
        
        # base case
        if len(lists)==1:
            return lists[0]
        
        # recursive case
        else:
            n = len(lists) // 2 
            left = self.mergeKLists(lists[:n])
            right = self.mergeKLists(lists[n:])
            combine_result = self.merge([left, right])
            
            return combine_result
            
    def merge(self, lists):
        ans = []
        while lists != [None, None]:
            if lists[0] == None:
                ans.append(lists[1].val)
                if lists[1].val != None:
                    lists[1] = lists[1].next
            elif lists[1] == None:
                ans.append(lists[0].val)
                if lists[0].val != None:
                    lists[0] = lists[0].next                
            elif lists[0].val < lists[1].val:
                ans.append(lists[0].val)
                if lists[0].val != None:
                    lists[0] = lists[0].next
            else:
                ans.append(lists[1].val)
                if lists[1].val != None:
                    lists[1] = lists[1].next
        
        if ans == []:
            return None
        
        last_val = None
        output = ListNode()
        for i in ans[::-1]:
            output.val = i
            output.next = last_val
            last_val = ListNode(i, last_val)
        
        return output
```

**time:**

![method 1](./pics/m1.png)

**method 2:**

[Code Source](https://leetcode.com/problems/merge-k-sorted-lists/discuss/10919/Python-easy-to-understand-divide-and-conquer-solution.)

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        
        # base case
        if len(lists)==1:
            return lists[0]
        
        # recursive
        n = len(lists) // 2 
        left = self.mergeKLists(lists[:n])
        right = self.mergeKLists(lists[n:])
        result = self.merge(left, right)
        return result
            
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
```

**time:**

![method 2](./pics/m2.png)

## 164. Maximum Gap

[Problem link](https://leetcode.com/problems/maximum-gap/)

**code:**

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return self.sort(nums)[1]
    
    def sort(self, nums):
        if len(nums) == 1:
            return nums, 0
        else:
            n = len(nums)//2
            left, _ = self.sort(nums[:n])
            right, _ = self.sort(nums[n:])
            final, max_val = self.merge(left, right)
            return final, max_val
    
    def merge(self, left, right):
        i = j = 0
        max_val = 0
        num = None
        ans = []
        for idx in range(len(left)+len(right)):
            if i==len(left):
                num = right[j]
                j+=1
            elif j==len(right):
                num = left[i]
                i+=1
            elif left[i] <= right[j]:
                num = left[i]
                i+=1
            elif right[j] < left[i]:
                num = right[j]
                j+=1
            ans.append(num)
            if idx == 0:
                continue
            if (num - ans[idx-1])>max_val:
                max_val = num - ans[idx-1]
        return ans, max_val
```

**time:**

![method 2](./pics/23m1.png)