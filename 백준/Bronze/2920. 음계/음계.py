import sys

list = list(map(int, sys.stdin.readline().split()))
number = [1, 2, 3, 4, 5, 6, 7, 8]

if list == number:
    print("ascending")
elif list == number[::-1]:
    print("descending")
else:
    print("mixed")