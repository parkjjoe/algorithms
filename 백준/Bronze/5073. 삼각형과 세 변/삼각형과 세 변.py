import sys

while 1:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b == c == 0:
        break

    if a >= b + c or b >= a + c or c >= a + b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    elif a != b and b != c and c != a:
        print("Scalene")