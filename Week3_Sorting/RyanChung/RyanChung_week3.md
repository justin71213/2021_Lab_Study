### 題目 [No.164 Maximum Gap](https://leetcode.com/problems/maximum-gap/)
>Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

>You must write an algorithm that runs in **linear time** and uses **linear extra space**.

>Example 1:  
>Input: nums = [3,6,9,1]  
>Output: 3

### Radix Sort   

將十進位切成十個 bucket，再把陣列中的數字逐個放入  
放入方法：**LSB** to **MSB**  

![](https://i.imgur.com/7iPUkfC.png)

>1. The first step is to find the maximum value in nums array, it will be the threshold to end while loop.
>2. Then use the radix sort algorithm to sort based on each digit from Least Significant Bit
(LSB) to Most Significant Bit (MSB), that's exactly what's showing in the link.
>3. `(nums[i] / exp) % 10` is used to get the digit, for each digit, basically the digit itself serves as the index to access the count array.
>4. Count array stores the index to access aux
array which stores the numbers after sorting based on the current digit.
>5. Finally, find the maximum gap from sorted array.

這邊有個 [動態演示](https://www.cs.usfca.edu/~galles/visualization/RadixSort.html)

範例 Code：[Radix sort solution in Java with explanation](https://leetcode.com/problems/maximum-gap/discuss/50642/Radix-sort-solution-in-Java-with-explanation)  
```java
public class Solution {
public int maximumGap(int[] nums) {
    if (nums == null || nums.length < 2) {
        return 0;
    }
    
    // m is the maximal number in nums
    int m = nums[0];
    for (int i = 1; i < nums.length; i++) {
        m = Math.max(m, nums[i]);
    }
    
    int exp = 1; // 1, 10, 100, 1000 ...
    int R = 10; // 10 digits

    int[] aux = new int[nums.length];
    
    while (m / exp > 0) { // Go through all digits from LSB to MSB
        int[] count = new int[R];
        
        for (int i = 0; i < nums.length; i++) {
            count[(nums[i] / exp) % 10]++;
        }
        
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }
        
        for (int i = nums.length - 1; i >= 0; i--) {
            aux[--count[(nums[i] / exp) % 10]] = nums[i];
        }
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = aux[i];
        }
        exp *= 10;
    }
    
    int max = 0;
    for (int i = 1; i < aux.length; i++) {
        max = Math.max(max, aux[i] - aux[i - 1]);
    }
     
    return max;
}
}
```
Runtime: 138 ms	(15%)  
Memory: 54 MB (28%)  
...好像也沒很快  

### 用 Linked List 實作 Radix Sort in C
```c
struct node{
	int number;
	struct node *next;
};

struct node *add_node (int n) { 
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->number = n;
    new_node->next = NULL;
    return new_node;
};

int find_largest_num (int* array, int size) {    
    int num = 0;      
    for (int i=0; i<size; i++) {
        if (array[i] > num)
            num = array[i];
    } 
    return num;
}

int get_num (int* array, int size) {
    int num = 0; 
    int new = 0; 
    for (int i=1; i<size; i++) {
        new = array[i]-array[i-1];
        if (new > num)
            num = new;
    } 
    return num;
}

int maximumGap(int* nums, int numsSize){     
    if (numsSize<2) {
        return 0;
    }
    
    int n = 1; // 1, 10, 100, 1000 ...
    int LargestNum = find_largest_num(nums, numsSize);
    struct node* current = (struct node*)malloc(sizeof(struct node));
    struct node* digit[10];
    for (int i=0; i<10; i++){
        digit[i] = malloc(sizeof(struct node));
        digit[i]->number = 0;
        digit[i]->next = NULL;
    }
    
    while (LargestNum/n > 0) {
        
        // Radix Sort
        for (int i=0; i<numsSize; i++){
            current = digit[(nums[i]/n) % 10];
            while (true) {
                if (current->next == NULL) {
                    current->next = add_node(nums[i]);
                    break;
                }
                else{
                    current = current->next;
                }
            }
        }
        // resorting nums
        int index = 0;
        for (int i=0; i<10; i++){
            current = digit[i];
            while (true) {
                if (current->next == NULL) {
                    break;
                }
                else{
                    nums[index] = current->next->number;
                    current = current->next;
                    index++;
                }
            }
        }
        for (int i=0; i<10; i++){
            digit[i]->number = 0;
            digit[i]->next = NULL;
        }  
        n *= 10;
    }
    return get_num(nums,numsSize);
}
```
結果：<span style="color:tomato;">Time Limit Exceeded !</span>

可能的解法：stackoverflow 有人解釋 [如何優化](https://stackoverflow.com/questions/67750089/radix-sort-using-array-of-linked-list-as-bin-in-c)

>Studying your approach, I'm afraid the complexity is far above the expected O(n) or more precisely O(n.log(max_value)). Here are some sources of concern:
>- allocating and freeing a list element for each entry in the array for each pass is very costly and may add a non linear complexity factor.
>- searching for the last list element to append the element is a linear search, which translates into quadratic complexity for the iterated operation.

看起來我有問題(二)的可能性

用它給的結果：  
Runtime: 128 ms	(91%)  
Memory: 16.3 MB MB (50%)  

優化程度相當誇張：  
7419.397ms -> 0.864ms