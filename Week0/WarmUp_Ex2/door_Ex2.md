# [Leetcode 1. Two Sum](https://leetcode.com/problems/two-sum/)

Example:
```
Input: nums = [3,6,5,1,1010], target = 7
Output: [1,3]
```
Use **hash table**, because search key in hash table is O(1) time.  
In python, just store data to dictionary. 
```
key = target - nums[i]  
value = i
and check the coming nums[i] is in dict or not.
```
| key | value |
| -------- | -------- | 
| 4     |  -1    |  
| 1     |  1    |  
| 2     |  2    |  
| 6     |  -1    |  
| -1003     |  0    |   

In C, you need to build hash table by youself.  
`H(x) = (target - nums[i]) mod 1009`
| key | value |next value |
| -------- | -------- | -------- | 
| 0     |  -1    |    NULL    | 
| 1     |  1    |   4    | 
| 2     |  2    |   NULL    |
| 3     |  -1    |   NULL    |
| 4     |  0    |   NULL    |
| 5     |  0    |   NULL    |
| 6     |  3    |   NULL    |

## Code
```c
#include <stdio.h>
#include <stdlib.h>
#define PRIME 1009

struct bucket {
  int value;
  struct bucket *next;
};
int hash(int key) { return abs((key % PRIME)); }
void init_ht(struct bucket *ht) {
  int i;
  for (i = 0; i < PRIME; i++) {
    ht[i].value = -1;
    ht[i].next = NULL;
  }
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  int *result = (int *)malloc(sizeof(int) * 2);
  // create hash table
  struct bucket *ht = (struct bucket *)malloc(sizeof(struct bucket) * PRIME);
  init_ht(ht);

  for (int i = 0; i < numsSize; i++) {
    int pos = hash(nums[i]);
    if (ht[pos].value == -1) // not exist
    {
      int insert_pos = hash(target - nums[i]);
      ht[insert_pos].value = i;
    } else {
      if (nums[ht[pos].value] == target - nums[i] &&
          ht[pos].value != i) { // get answer
        result[0] = ht[pos].value;
        result[1] = i;
        return result;
      } else {
        struct bucket *t = ht[pos].next;
        while (t) {
          if (nums[t->value] == target - nums[i] &&
              t->value != i) { // get answer
            result[0] = t->value;
            result[1] = i;
            return result;
          } else
            t = t->next;
        }
        // collision
        struct bucket *new = (struct bucket *)malloc(sizeof(struct bucket));
        new->value = i;
        new->next = ht[pos].next;
        ht[pos].next = new;
      }
    }
  }
  return NULL;
}
```