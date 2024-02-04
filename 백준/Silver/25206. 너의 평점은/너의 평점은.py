import sys

total = 0 # 분모
sum = 0 # 분자

for _ in range(20):
    a = list(map(str, sys.stdin.readline().rstrip().split()))

    if a[2] == "P":
        pass
    else:
        total += float(a[1])

    if a[2] == "A+":
        sum += float(a[1]) * 4.5
    elif a[2] == "A0":
        sum += float(a[1]) * 4.0
    elif a[2] == "B+":
        sum += float(a[1]) * 3.5
    elif a[2] == "B0":
        sum += float(a[1]) * 3.0
    elif a[2] == "C+":
        sum += float(a[1]) * 2.5
    elif a[2] == "C0":
        sum += float(a[1]) * 2.0
    elif a[2] == "D+":
        sum += float(a[1]) * 1.5
    elif a[2] == "D0":
        sum += float(a[1]) * 1.0
    elif a[2] == "P":
        pass
    else:
        sum += 0.0

print(sum / total)