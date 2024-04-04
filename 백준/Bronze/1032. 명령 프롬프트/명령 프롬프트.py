import sys

n = int(sys.stdin.readline())
word = list(sys.stdin.readline().rstrip())

for _ in range(n - 1):
    new_word = list(sys.stdin.readline().rstrip())

    for i in range(len(word)):
        if word[i] != new_word[i]:
            word[i] = "?"

print("".join(word))