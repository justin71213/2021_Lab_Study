def calculate(s):
    #
    alist = []
    num = ""
    for idx, char in enumerate(s):
        if char == " ":
            continue
        if char.isnumeric():
            num += char
        if (not char.isnumeric()) or (idx == len(s) - 1):
            alist.append(num)
            num = ""
        if (char == "+") or (char == "-") or (char == "(") or (char == ")"):
            alist.append(char)
    print(alist)
    # base case
    if "(" not in alist:
        add = True
        val = 0
        for char in alist:
            if char == "+":
                add = True
            elif char == "-":
                add = False
            elif char.isnumeric():
                if add:
                    val += int(char)
                else:
                    val -= int(char)
        return val

    # recursive
    else:
        stack = []
        val = 0
        for idx in range(len(alist)):
            if alist[idx] == " ":
                continue
            if alist[idx] == "(":
                stack.append(idx)
            elif alist[idx] == ")":
                start = stack.pop()
                end = idx
                val += calculate(alist[start + 1 : end])
        return val


if __name__ == "__main__":
    # s = "20+30"
    s = "(1+2+(3+4)+5)"
    # s = " 2-1 + 2 "
    # s = "2147483647"
    # s = "(1+(4+5+2)-3)+(6+8)"
    print(calculate(s))
