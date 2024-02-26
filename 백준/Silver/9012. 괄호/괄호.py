import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = list(str(sys.stdin.readline().rstrip()))
    count = 0

    for i in range(len(stack)):
        if stack[i] == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            print("NO")
            break

    if count > 0:
        print("NO")
    elif count == 0:
        print("YES")