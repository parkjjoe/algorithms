import sys

while 1:
    sentence = str(sys.stdin.readline().rstrip())

    if sentence == ".":
        break

    stack = []

    for i in sentence:
        if "(" in i:
            stack.append("(")
        elif ")" in i:
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        elif "[" in i:
            stack.append("[")
        elif "]" in i:
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")