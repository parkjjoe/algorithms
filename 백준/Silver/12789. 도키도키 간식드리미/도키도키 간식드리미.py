import sys

n = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))

start = 1
new_line = []

while student:
    if student[0] != start:
        new_line.append(student.pop(0))
    else:
        student.pop(0)
        start += 1

    while new_line:
        if new_line[-1] == start:
            new_line.pop()
            start += 1
        else:
            break

if len(new_line) == 0:
    print("Nice")
else:
    print("Sad")