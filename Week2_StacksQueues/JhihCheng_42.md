# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## 題目敘述
輸入一串數字陣列，計算所有間隔間的容量總和，例如:<br>
![](https://i.imgur.com/KjOn5X2.png)
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```
## 解題邏輯:
從頭尾各掃描一次計算從該視角看出去的容量，取重疊部分(最小值)

## 程式碼
```c
int min(int a, int b){
    if (a<b){
        return a;
    }
    else{
        return b;
    }
}

int trap(int* height, int heightSize){

    int leftIndex=0;
    int i;
    int tmp;
    int sum = 0;
    if(heightSize <= 0){return 0;}
    int stack[heightSize];
    int rightIndex = heightSize -1;
    for(i = 0 ;i<heightSize ;i++){
        if(height[leftIndex]<= height[i]){
            leftIndex = i;
        }
        //實作Stack出了點問題，不然應該要用push
        stack[i] = height[leftIndex] - height[i];
    }
    printf("\n");
    for(i = rightIndex ;i>=0 ;i--){
        if(height[rightIndex]<= height[i]){
            rightIndex = i;
        }
        //這裡使用pop
        sum+= min(height[rightIndex]-height[i],stack[i]);
    }
    return sum;
}
```
## 執行結果
```
Runtime: 4 ms, faster than 90.45% of C online submissions for Trapping Rain Water.
Memory Usage: 6.3 MB, less than 98.14% of C online submissions for Trapping Rain Water.
```

## 實作Stack
```c
// Linked list結構
typedef struct stacknode{
    int num; //資料內容
    struct stacknode* ptr; //底下那層的指標
}stack;

// Stack頂端
struct stacknode *top;

void push(int content){
    stack *new_node = malloc(sizeof(stack));
    new_node -> ptr = top;
    new_node -> num = content;
    top = new_node;

}

int pop(){
    if(!top){
        return -1;
    }
    stack* tmp = top;
    int element = top -> num;
    top = top -> ptr;
    free(tmp);

    return element;
}

int min(int a, int b){
    if (a<b){
        return a;
    }
    else{
        return b;
    }
}

int trap(int* height, int heightSize){

    if(heightSize <= 0){return 0;}
    int i;
    int sum = 0;
    int leftIndex=0;
    top = NULL;
    int rightIndex = heightSize -1;
    
    for(i = 0 ;i<heightSize ;i++){
        if(height[leftIndex]<= height[i]){
            leftIndex = i;
        }
        push((height[leftIndex] - height[i]));
    }
    
    for(i = rightIndex ;i>=0 ;i--){
        if(height[rightIndex]<= height[i]){
            rightIndex = i;
        }
        sum+= min(height[rightIndex]-height[i],pop());
    }
    return sum;
}

```

## 執行結果
```
Runtime: 4 ms, faster than 90.43% of C online submissions for Trapping Rain Water.
Memory Usage: 7.4 MB, less than 11.44% of C online submissions for Trapping Rain Water.
```
## 資料來源
Leet code solution<br>
[用C語言製作堆疊(Stack)](https://lakesd6531.pixnet.net/blog/post/332858496)<br>
[以陣列 (Array) 為基礎的堆疊 (Stack)](https://opensourcedoc.com/data-structures-in-c/stack-in-array/)
