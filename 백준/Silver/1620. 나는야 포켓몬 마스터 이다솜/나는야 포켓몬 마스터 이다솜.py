import sys

n, m = map(int, sys.stdin.readline().split())

dict = {}
count = 1

for _ in range(n):
    pokemon = str(sys.stdin.readline().rstrip())
    dict[pokemon] = count
    count += 1

dict_reverse = {v: k for k, v in dict.items()}

for _ in range(m):
    question = sys.stdin.readline().rstrip()
    if question in dict.keys():
        print(dict[question])
    else:
        print(dict_reverse[int(question)])