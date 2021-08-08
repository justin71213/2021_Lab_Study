# 23. Merge k Sorted Lists

## method 1

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
            left_sorted = self.mergeKLists(lists[:n])
            right_sorted = self.mergeKLists(lists[n:])
            combine_result = self.merge([left_sorted, right_sorted])
            
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
            elif lists[0].val <= lists[1].val:
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

## method 2

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
