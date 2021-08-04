class Solution:
    def calculate(self, s):
        """
        https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack./183875
        """
        num = 0
        stack = []  # 用來儲存算好的數值，最後是回傳 sum(stack)，乘除需先算好
        last_sign = "+"
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


if __name__ == "__main__":
    s = "10-3/2"
    # s = "3+2*2"
    # s = "1+2+3"
    # s = "2*3*4"
    # s = "   -20*5+10*5+10*5"
    # s = " 3+5 / 2 "
    # s = "3/4"
    # s = "3+2*2"
    # s = "2*3 - 4/2"
    # s = "9/10"
    # s = "1*2-3/4+5*6-7*8+9/10"
    print("output:", Solution().calculate(s))
