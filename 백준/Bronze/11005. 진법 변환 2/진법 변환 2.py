import sys

n, b = map(int, sys.stdin.readline().rstrip().split())
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

while n:
    answer += array[n % b] # 주어진 수를 원하는 진법 수로 나눔.
    n //= b # 주어진 수는 나눈 후의 나머지로 대체

answer = answer[::-1] # 진법 처리를 위한 역순
print(answer)