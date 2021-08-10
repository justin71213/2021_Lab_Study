# 164. Maximum Gap
## description
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week3_Sorting/XiangWei_164/description.png)
## background
1. comparison-based algorithm: at most O(nlogn)
  - insertion sort
  - bubble sort
  - selection sort
  - heap sort
  - merge sort
  - quick sort<br>
  
2. non-comparison-based algorithm: at most O(n)
  - counting sort
  - bucket sort:O(n+k)
  - radix sort

[各種sort參考](https://rust-algo.club/sorting/insertion_sort/index.html)<br>
此題用bucket sort解

### bucket sort
```
bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
.......a) Insert arr[i] into bucket[n*array[i]]
        ps:insertion can be implemented using linked list in C, vector in c++
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
```
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Bucket_sort_1.svg/1200px-Bucket_sort_1.svg.png)

## flow
1. bucket sort
2. To find maximum difference between two successive elements,traverse the sorted elements.
## code
```cpp
void bucketSort(vector<int>& nums, int n)
{
    int max = 0;
    //找出最大值
    for(int i=0;i<n;i++){
        if(nums[i]>max){
            max = nums[i];
        }
    }
    //用最大值找bucket size
    //int bucket_size = max/n==0 ? 1 : max/n;
    int bucket_size = 300000000;
    // 1) Create n empty buckets
    int num = max/bucket_size+1;
    vector<int> b[num];
 
    // 2) Put array elements
    // in different buckets
    for (int i = 0; i < n; i++) {
        int bi = nums[i]/bucket_size; // Index in bucket
        b[bi].push_back(nums[i]);
    }
 
    // 3) Sort individual buckets
    for (int i = 0; i < num; i++)
        sort(b[i].begin(), b[i].end());
 
    // 4) Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < num; i++)
        for (int j = 0; j < b[i].size(); j++)
            nums[index++] = b[i][j];
}
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        bucketSort(nums, n);
        int max = 0;
        for(int i=1;i<n;i++){
            int temp=nums[i] - nums[i-1];
            if(temp>max){
                max = temp;
            }
        }
        return max;
    }
};
```
## result
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week3_Sorting/XiangWei_164/result.png)
## reference
1.https://www.geeksforgeeks.org/bucket-sort-2/
