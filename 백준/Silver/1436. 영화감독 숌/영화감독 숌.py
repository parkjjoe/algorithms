import sys

n = int(sys.stdin.readline())
count = 0
number = 0

while 1:
    if str(666) in str(number): # number에 666이 포함돼 있으면 count 1 증가
        count += 1

    if count == n:
        print(number)
        break

    number += 1 # count가 n과 같아질 때까지 number를 1씩 증가시키면서 while문 반복