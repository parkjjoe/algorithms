import sys
from collections import Counter

n = int(sys.stdin.readline())

num = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

print(round(sum(num) / len(num)))
print(num[len(num) // 2])

count = Counter(num).most_common(2) # 빈도 수가 높은 수 2개 가져오기

if len(num) > 1:
    if count[0][1] == count[1][1]: print(count[1][0])
    else: print(count[0][0])
else: print(count[0][0])

print(max(num) - min(num))