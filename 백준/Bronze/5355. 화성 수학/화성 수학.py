import sys

t = int(sys.stdin.readline())

for _ in range(t):
    eq = list(map(str, sys.stdin.readline().rstrip().split()))
    number = float(eq[0])

    for i in range(1, len(eq)):
        if eq[i] == "@":
            number *= 3
        elif eq[i] == "%":
            number += 5
        elif eq[i] == "#":
            number -= 7

    print(f"{number:.2f}")