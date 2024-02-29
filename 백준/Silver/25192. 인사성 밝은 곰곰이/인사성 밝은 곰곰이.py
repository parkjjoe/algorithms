import sys

n = int(sys.stdin.readline())

count = 0
people = set()

for _ in range(n):
    chat = str(sys.stdin.readline().rstrip())

    if chat == "ENTER":
        count += len(people)
        people = set()
    else:
        people.add(chat)

count += len(people)

print(count)