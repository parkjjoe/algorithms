import sys

s = sys.stdin.readline().rstrip()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i in s:
        print(s.index(i), end = " ")
    else:
        print("-1", end = " ")