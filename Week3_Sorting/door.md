# [Leetcode 23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
## Solution
Use [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))  


### python
In python3, use [heapq](https://docs.python.org/3/library/heapq.html) library.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # Check for input:[]
            return ListNode().next

        heap = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heap.append(tuple((lists[i].val, i, lists[i])))

        if not heap:  # Check for input:[[]]
            return ListNode().next

        heapq.heapify(heap)

        head = tail = None
        while heap:
            i, node = heapq.heappop(heap)[1:]
            if head is None:  # First element
                head = tail = node
            else:
                tail.next = node
                tail = node

            if node.next:
                heapq.heappush(heap, (tail.next.val, i, tail.next))

        return head
```
#### Time complexity analysis
Take **O(k)**
```python
for i in range(len(lists)):
    if not lists[i]:
        continue
    heap.append(tuple((lists[i].val, i, lists[i])))
```
By the way, if elements in heapq.heapify are `heap.append(tuple((lists[i].val, lists[i])))`
![](https://i.imgur.com/7x5oN7U.png)

Take **O(k)**  
reference: https://www.growingwiththeweb.com/data-structures/binary-heap/build-heap-proof/
```python
heapq.heapify(heap)
```
in `while heap:` Take **O( n + (n-k) log k)**  , n is total value numbers.  
Take **O(1)**
```python
i, node = heapq.heappop(heap)[1:]
```
Take **O(log k)**
```python
if node.next:
    heapq.heappush(heap, (tail.next.val, i, tail.next))
```
### C++
Libray: 
- https://www.cplusplus.com/reference/algorithm/make_heap/
- https://www.geeksforgeeks.org/heap-using-stl-c/

Comparator example: https://stackoverflow.com/questions/2574060/c-min-heap-with-user-defined-type

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <iostream>
#include <vector>
using namespace std;

struct greater1 {
  bool operator()(ListNode* a, ListNode* b) const { return a->val > b->val; }
};

class Solution {
 public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    vector<ListNode*> heap;
    for (auto node : lists) {
      if (!node) continue;
      heap.push_back(node);
    }
    if (heap.empty()) return NULL;
    make_heap(heap.begin(), heap.end(), greater1());

    struct ListNode* head = NULL;
    struct ListNode* tail = NULL;

    while (!heap.empty()) {
      pop_heap(heap.begin(), heap.end(), greater1());
      ListNode* pop_node = heap.back();
      heap.pop_back();
      if (!head)
        head = tail = pop_node;
      else {
        tail = tail->next = pop_node;
      }
      if (pop_node->next) {
        heap.push_back(pop_node->next);
        push_heap(heap.begin(), heap.end(), greater1());
      }
    }

    return head;
  }
};
```
### C
Build heap by myself.
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void swap(struct ListNode** heap, int i, int j) {
  struct ListNode* tmp = heap[i];
  heap[i] = heap[j];
  heap[j] = tmp;
}
void print_heap(struct ListNode** heap, int heap_count) { // For debug
  int i = 1;
  printf("Heap:");
  while (i <= heap_count) printf("%d ", heap[i++]->val);
  printf("\n");
}

void heapify(struct ListNode** heap, int i, int heap_count) {
  if (!heap_count) return;
  int comp_index;
  if (2 * i > heap_count)  // No child
    return;
  else if (2 * i + 1 > heap_count)  // Only left child
    comp_index = 2 * i;
  else
    comp_index = heap[2 * i]->val < heap[2 * i + 1]->val ? 2 * i : 2 * i + 1;

  if (heap[i]->val > heap[comp_index]->val) {
    swap(heap, i, comp_index);
    heapify(heap, comp_index, heap_count);
  }
}
void build_min_heap(struct ListNode** heap, int heap_count) {
  for (int i = heap_count / 2; i >= 1; i--)
    heapify(heap, i, heap_count);
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
  struct ListNode* heap[listsSize + 1];
  if (!listsSize) return NULL;
  int heap_count = 0;
  for (int i = 0; i < listsSize; i++) {
    if (!lists[i]) continue;
    heap_count++;
    heap[heap_count] = lists[i];
  }
  if (!heap_count) return NULL;
  build_min_heap(heap, heap_count);
  struct ListNode* head = NULL;
  struct ListNode* tail = NULL;
  do {
    struct ListNode* pop_min = heap[1];
    if (!head)
      head = tail = pop_min;
    else
      tail = tail->next = pop_min;
    if (pop_min->next)
      heap[1] = heap[1]->next;
    else {
      swap(heap, 1, heap_count);
      heap_count--;
    }
    heapify(heap, 1, heap_count);
  } while (heap_count);

  return head;
}
```