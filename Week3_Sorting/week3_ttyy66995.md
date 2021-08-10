### [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
![](https://i.imgur.com/89gFkBA.png)

**解題羅技：**
先將各list中第一個數(最小)放進priority_queue(存放pair<int, link*>)中，因為priority_queue會排序，再將最上面的一個取出(pop)放入答案，若取出的node有point的話則將它指向的pair放入放進priority_queue
```{ c++
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
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        ListNode *root=new ListNode();
        ListNode *curr=root;  
          
        priority_queue<pair<int,ListNode*>, vector<pair<int,ListNode*>> , greater<pair<int,ListNode*>> > pq;
        
        for(auto i:lists){
            if(i != NULL)      
                pq.push({i->val,i});
                
        }
        
        if(pq.empty()){
            return NULL;
        }
        
        
        while(!pq.empty()){
            auto top_node = pq.top();
            curr->next= top_node.second;   
            curr = curr->next;  
            
            pq.pop();
            
            if(top_node.second->next) {
                pq.push({top_node.second->next->val,top_node.second->next});
            }
        }
         
        return root->next;
    }
};
}
```
![](https://i.imgur.com/mTNZZhz.png)