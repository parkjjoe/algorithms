import sys

n = str(sys.stdin.readline().rstrip())

for i in n:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()

    print(i, end="")