import sys

n = int(sys.stdin.readline())

def tower(n, start, end): # 원판 개수, 시작 장대, 끝 장대
    if n == 1:
        return print(start, end)

    tower(n - 1, start, 6 - start - end)
    print(start, end)
    tower(n - 1, 6 - start - end, end)

print(2 ** n - 1)
tower(n, 1, 3)