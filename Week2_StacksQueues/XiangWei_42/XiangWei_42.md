# 42. Trapping Rain Water

## discription
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week2_StacksQueues/XiangWei_42/discription.png)

## flow
 
1. 會有水的地方：讀到更大的數字時
2. 突破前高時，表示水被分區了
```
for new value{
  if value > max:
    結算前一區的水量並清空stack
  else if value > last_value:
    填滿stack比value還低的水量，並記在stack中
  else:
    push to stack
}  
```
example1<br>
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week2_StacksQueues/XiangWei_42/discription.png)
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week2_StacksQueues/XiangWei_42/flow1.png)
example2<br>
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week2_StacksQueues/XiangWei_42/flow2.png)
## code
```c
struct Stack {
    int top;
    unsigned capacity;
    int* array;
    int max;
};
 
// function to create a stack of given capacity. It initializes size of
// stack as 0
struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    stack->max = 0;
    return stack;
}
 
// Stack is full when top is equal to the last index
int isFull(struct Stack* stack)
{
    return stack->top == stack->capacity - 1;
}
 
// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}
 
// Function to add an item to stack.  It increases top by 1
void push(struct Stack* stack, int item)
{
    if (isFull(stack))
        return;
    stack->array[++stack->top] = item;
    
}
 
// Function to remove an item from stack.  It decreases top by 1
int pop(struct Stack* stack)
{
    if (isEmpty(stack)){
        
        return INT_MIN;
    }
        
    
    return stack->array[stack->top--];
}
 
// Function to return the top from stack without removing it
int peek(struct Stack* stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top];
}

int trap(int* height, int heightSize){
    int result = 0;

    
    struct Stack* stack = createStack(heightSize);
    
    for(int i=0;i<heightSize;i++){
        int current = height[i];
        if(i == 0){
            push(stack,current);
            stack->max = current;
        }
        else{
            //完整一區
            
            if(current >= stack->max){
                int num = stack->top;
                for(int j=0 ; j< num; j++){
                   
                    result += stack->max - pop(stack);
                }
                int a = 0;
                a = pop(stack);
                
                push(stack, current);
                stack->max = current;
            }
            else if(current > peek(stack)){
                int count = 0;
                while(true){
                    if(peek(stack) < current){
                        result += current - pop(stack);
                        count += 1;
                    }
                    else{
                        break;
                    }
                }
                for(int k=0; k<=count; k++){
                    push(stack,current);
                }       
            }
            else{
                push(stack,current);
            }
        }
    }
    return result;
}
```


## result
![](https://github.com/justin71213/2021_Lab_Study/blob/XiangWei/Week2_StacksQueues/XiangWei_42/submission.png)

