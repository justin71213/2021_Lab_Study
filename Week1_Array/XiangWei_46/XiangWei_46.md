# 46. Permutations
## discription
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

## flow
以排列ABC為例：
1. A開頭，排列BC
    - B開頭，排列C
    - C開頭，排列B
2. B開頭，排列AC
    - A開頭，排列C
    - C開頭，排列A
3. C開頭，排列AB
    - B開頭，排列A
    - A開頭，排列B

![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week1_Array/XiangWei_46/explanation.png)
## code
``` C
// 交換list[a],list[b]的值
void swap(int *list, int a, int b){
    int temp = list[a];
    list[a] = list[b];
    list[b] = temp;
}

//目的是為了算階乘
int Factorial(int n) {
    if(n == 1) 
        return 1;
    else
        return n * Factorial(n - 1); 
}


int temp_row = 0; //存放至result的第幾列，以temp_row紀錄
//對list的start位置到stop位置排列
void permutation(int *list, int start, int stop, int **result){
    if(start != stop){
        for(int i=start; i <= stop; i++){
            swap(list,start,i);
            permutation(list, start+1, stop, result);
            swap(list,start,i);
        }
    }
    //遞迴的終止點
    else{
        for(int i=0; i<= stop; i++){
            result[temp_row][i] = list[i];
        }
        temp_row += 1;
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){

    //計算結果會有幾列,ex:[1,2,3]會有６列
    int row = Factorial(numsSize);
    
    //配置row個指標
    int **result = (int **)malloc(row * sizeof(int *));
    
    //為每個row配置numsSize個int的空間
    for (int i=0; i<row; i++)
        result[i] = (int *)malloc(numsSize * sizeof(int)); 
    //開始排列
    permutation(nums,0,numsSize-1,result);
    
    //for leetcode
    //跟leetcode說每個row的大小
    *returnColumnSizes = (int *)malloc(sizeof(int) * row);
    for(int i=0;i<row;i++){
        (*returnColumnSizes)[i] = numsSize;
    }
    //跟leetcode說有幾個row
    *returnSize = row;
    
    //因為temp_row是全域變數，在permite()結束前，讓temp_row歸零。
    temp_row = 0;
    
    return result;
}


```
  
## result
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week1_Array/XiangWei_46/result.png)

## key word
1. [指標與陣列](https://ivan7645.github.io/2017/01/11/ptr_multi_arr/)
2. 遞迴
