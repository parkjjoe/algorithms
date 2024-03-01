import sys

n, m = map(int, sys.stdin.readline().split())

word = {}

for _ in range(n):
    string = str(sys.stdin.readline().rstrip())

    if len(string) < m:
        continue
    else:
        if string in word:
            word[string] += 1
        else:
            word[string] = 1

word = sorted(word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in word:
    print(i[0])