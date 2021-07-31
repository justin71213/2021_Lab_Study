# Basic Calculator
- [LeetCode 224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) 
- [LeetCode 227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
- [LeetCode 772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)

Implement a basic calculator to evaluate a simple expression string.

The expression string contains:
- non-negative integers
- `+` operator
- `-` operator
- `*` operator
- `/` operator 
- `^` operator
- open `(` and closing parentheses `)` 
- empty spaces

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [`-2147483648`, `2147483647`].

Some examples:
```
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
"2^3*4" = 32
```
## Solution
### 1.
---
Approach: Use Stacks

We will use two stacks

- Operand stack: This stack will be used to keep track of numbers.
- Operator stack: This stack will be used to keep operations [`+`, `-`, `*`, `/`, `^`,`(`]

Order of precedence of operations:

0. `(` for out-stack
1. `^` 
2. `/` `*`
3. `+` `–`
4. `(` for in-stack, `)` for out-stack

**Algorithm:**

Iterate through given expression, one character at a time.

1. If the character is an operand, push it to the operand stack.
2. If the character is an operator,
    1. If the operator stack is empty then push it to the operator stack.
    2. Else If the operator stack is not empty,
        1. If the character’s precedence is greater than or equal to the precedence of the stack top of the operator stack, then push the character to the operator stack.
        2. If the character’s precedence is less than the precedence of the stack top of the operator stack then do Process (as explained above) until character’s precedence is less or stack is not empty.
3. If the character is “(“, then push it onto the operator stack.
4. If the character is “)”, then do Process (as explained above) until the corresponding “(” is encountered in operator stack. Now just pop out the “(“.

Once the expression iteration is completed and the operator stack is not empty, do Process until the operator stack is empty.  The values left in the operand stack is our final result.

---

```c++
#include <stack>
typedef struct {
  string op;
  int pri_in;
  int pri_out;
} operator_t;
int myPow(int base, int exp) {
  int res = 1;
  for (int i = 0; i < exp; i++) res *= base;
  return res;
}
class Solution {
 public:
  int calculate(string s) {
    s += "+";
    stack<int> operand_stack;
    stack<operator_t> operator_stack;
    string no_str = "";
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == ' ')  // space
        continue;
      else if ('0' <= s[i] && s[i] <= '9') {  // number
        no_str += s[i];
      } else {  // operator
        if (no_str != "") {
          operand_stack.push(stoi(no_str));
          no_str = "";
        }
        operator_t tmp;
        tmp.op = s[i];
        // Set priority
        if (s[i] == ')')
          tmp.pri_out = 4;
        else if (s[i] == '(') {
          tmp.pri_out = 0;
          tmp.pri_in = 4;
        } else if (s[i] == '+' || s[i] == '-')
          tmp.pri_out = tmp.pri_in = 3;
        else if (s[i] == '*' || s[i] == '/')
          tmp.pri_out = tmp.pri_in = 2;
        else if (s[i] == '^')
          tmp.pri_out = tmp.pri_in = 1;

        // Adjust stack
        while (!operator_stack.empty() &&
               operator_stack.top().pri_in <= tmp.pri_out) {
          operator_t opt = operator_stack.top();
          operator_stack.pop();
          if (opt.pri_in == 4) break;
          int opr1 = operand_stack.top();
          operand_stack.pop();
          int opr2 = operand_stack.top();
          operand_stack.pop();

          int res;
          if (opt.pri_in == 3) {
            res = opt.op == "+" ? opr2 + opr1 : opr2 - opr1;
          } else if (opt.pri_in == 2) {
            res = opt.op == "*" ? opr2 * opr1 : opr2 / opr1;
          } else if (opt.pri_in == 1)
            res = myPow(opr2, opr1);

          operand_stack.push(res);
        }

        if (tmp.op != ")") operator_stack.push(tmp);
      }
    }
    if (no_str != "") operand_stack.push(stoi(no_str));

    return operand_stack.top();
  }
};
```
### 2.
Reference: https://leetcode.com/problems/basic-calculator-ii/discuss/63003/Share-my-java-solution

Add recursions to deal with `()`.
```c++
#include <stack>
int myPow(int base, int exp) {
  int res = 1, sign = 1;
  if (base < 0) {
    sign = -1;
    base *= -1;
  }
  for (int i = 0; i < exp; i++) res *= base;
  return res * sign;
}
class Solution {
 public:
  int calculate(string s) {
    s += "+";
    stack<int> stack;
    char sign = '+';
    int num = 0;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == ' ')  // space
        continue;
      else if ('0' <= s[i] && s[i] <= '9')  // number
        num = 10 * num + (s[i] - '0');
      else if (s[i] == '(') {
        for (int j = s.length() - 1; j < i; j--)
          if (s[j] == ')') num = calculate(s.substr(i + 1, j - i - 1));
      } else {  // operator
        if (sign == '+')
          stack.push(num);
        else if (sign == '-')
          stack.push(-num);
        else if (sign == '*') {
          int tmp = stack.top();
          stack.pop();
          stack.push(tmp * num);
        } else if (sign == '/') {
          int tmp = stack.top();
          stack.pop();
          stack.push(tmp / num);
        } else if (sign == '^') {
          int tmp = stack.top();
          stack.pop();
          stack.push(myPow(tmp, num));
        }
        sign = s[i];
        num = 0;
      }
    }
    int res = 0;
    while (!stack.empty()) {
      res += stack.top();
      stack.pop();
    }
    return res;
  }
};
```