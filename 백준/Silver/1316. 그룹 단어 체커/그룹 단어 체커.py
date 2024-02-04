import sys

n = int(sys.stdin.readline())
count = n

for _ in range(n):
    word = str(sys.stdin.readline().rstrip())

    for i in range(len(word)-1):
        if word[i] == word[i+1]: # 연속된 알파벳이면 pass
            pass
        elif word[i] in word[i+1:]: # 그 이후에 똑같은 알파벳이 있다면 count 1 빼고 끝
            count -= 1
            break

print(count)