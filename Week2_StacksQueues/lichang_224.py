class Solution:
    def calculate(self, s):
        """
        source: https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack
        """
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


if __name__ == "__main__":
    # s = "1-(5)"
    # s = "(1-(3-4))"
    # s = "- (3 + (4 + 5))"
    # s = " (2-1) + 2 "
    # s = "(6)-(8)-(7)+(1+(6))"
    # s = " 2-1 + 2 "
    s = "2-(5-6)"
    # s = "-20+30"
    # s = " 2-1 + 2 "
    # s = "(1+(2+3)+5)"
    # s = " 2-1 + 2 "
    # s = "2147483647"
    # s = "(1+(4+5+2)-3)+(6+8)"

    print("output:", Solution().calculate(s))


# class Solution:
#     def calculate(self, s: str) -> int:
#         # Preprocessing for n-ditit: O(n)
#         alist = []
#         num = ""
#         basecase = True
#         for idx, char in enumerate(s):
#             if char.isnumeric():
#                 num += char
#             if char == "(":
#                 basecase = False
#             if (not char.isnumeric()) or ((char.isnumeric()) and (idx == len(s) - 1)):
#                 if num != "":
#                     alist.append(num)
#                 num = ""
#             if (char == "+") or (char == "-") or (char == "(") or (char == ")"):
#                 alist.append(char)
#         # print("alist:", alist)

#         # base case
#         if basecase:
#             add = True
#             val = 0
#             last_char = None
#             for char in alist:
#                 if char == "+":
#                     add = True
#                 elif char == "-":
#                     add = False
#                     if last_char == "-":
#                         add = True
#                 elif char.isnumeric():
#                     if add > 0:
#                         val += int(char)
#                     else:
#                         val -= int(char)
#                 last_char = char
#             return val

#         # recursive
#         else:
#             stack = []
#             summa = 0
#             val = 0
#             add = True
#             last_char = None
#             for idx in range(len(alist[:])):
#                 if alist[idx] == "(":
#                     stack.append(idx)
#                 elif alist[idx] == ")":
#                     start = stack.pop()
#                     end = idx
#                     val = self.calculate(alist[start + 1 : end])

#                     if val > 0:
#                         alist[start : end + 1] = [str(val)] + [
#                             "" for i in range(len(alist[start : end + 1]) - 1)
#                         ]
#                     else:
#                         alist[start : end + 1] = ["-", str(val * -1)] + [
#                             "" for i in range(len(alist[start : end + 1]) - 2)
#                         ]

#             val = self.calculate(alist)
#             return val
