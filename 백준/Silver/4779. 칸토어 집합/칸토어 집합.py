import sys

def cut(a, b):
    if b == 1:
        return

    for i in range(a + b // 3, a + (b // 3) * 2):
        result[i] = " "

    cut(a, b // 3) # 왼쪽
    cut(a + b // 3 * 2, b // 3) # 오른쪽

while 1:
    try:
        n = int(sys.stdin.readline())

        result = ["-"] * (3 ** n)
        cut(0, 3 ** n)
        print("".join(result))
    except:
        break