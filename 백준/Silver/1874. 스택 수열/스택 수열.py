import sys

n = int(sys.stdin.readline())

stack, result = [], []
count = 1

for _ in range(n):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        result.clear()
        result.append("NO")
        break

for i in result:
    print(i)