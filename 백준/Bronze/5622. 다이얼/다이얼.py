import sys

a = list(str(sys.stdin.readline().rstrip()))
time = 0

for i in range(len(a)):
    if a[i] in "ABC":
        time += 3
    elif a[i] in "DEF":
        time += 4
    elif a[i] in "GHI":
        time += 5
    elif a[i] in "JKL":
        time += 6
    elif a[i] in "MNO":
        time += 7
    elif a[i] in "PQRS":
        time += 8
    elif a[i] in "TUV":
        time += 9
    else:
        time += 10

print(time)