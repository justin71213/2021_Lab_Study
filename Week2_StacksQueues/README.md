# Week2:Stacks Queues

## [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

**code:**

使用 stack 紀錄所有看到的數值，最後加總 stack 內的數值回傳。
[code source](https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack./183875)

```python
def calculate(self, s):
    num = 0 # digits
    stack = []  # 用來儲存算好的數值，最後是回傳 sum(stack)，乘除需先算好
    last_sign = "+" # 預設為正
    for idx in range(len(s)):
        if s[idx].isnumeric():
            num = 10 * num + int(s[idx])
        if (s[idx] in "+-*/") or (idx == len(s) - 1):
            if last_sign == "+":
                stack.append(num)
            elif last_sign == "-":
                stack.append(-num)
            elif last_sign == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            num = 0
            last_sign = s[idx]
    return sum(stack)
```

## [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

**code:**

使用 stack 紀錄括號前的總值以及括號外的正負號。
[code source](https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack)

```python
def calculate(self, s):
    total = 0  # 目前總值
    num = 0  # 數字 e.g. 20, 36,...
    sign = 1  # 正負號
    stack = []
    for idx, char in enumerate(s):
        if char.isnumeric():
            num = 10 * num + int(char)
        elif char in "+-":
            total += num * sign  # 累積數值
            num = 0  # 初始化數字
            # 先動完，在改正負號 e.g 20-30 -> 先加 0 + 20，再改 sing 為 -
            sign = [-1, 1][char == "+"]
        elif char == "(":
            stack.append(total)  # 把括號前的總值記錄到 stack，e.g. 10 -(2+3) 的 "10"
            stack.append(sign)  # 紀錄括號外的正負好 e.g. 10 -(2+3) 的 "-"
            sign = 1  # 初始化括號內部的正負號
            total = 0  ## 初始化括號內部的總值
        elif char == ")":
            total += num * sign  # 括號內的總值
            total *= stack.pop()  # 括號外的正負號
            total += stack.pop()  # 括號外的總值 +/- 括號內的總值
            num = 0  # 初始化數字

    return total + num * sign
```
