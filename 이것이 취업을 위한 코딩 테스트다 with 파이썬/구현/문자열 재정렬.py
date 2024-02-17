import sys

n = list(str(sys.stdin.readline().rstrip()))

alphabet = []
sum = 0

for i in n:
    if i.isalpha(): # 알파벳은 배열에 저장해서 나중에 정렬
        alphabet.append(i)
    else: # 숫자는 합 계산
        sum += int(i)

alphabet.sort()

print("".join(alphabet), sum, sep="")
