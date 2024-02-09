import sys

a, b, v = map(int, sys.stdin.readline().split())
day = (v - b) / (a - b) # a * day - b * (day - 1) = v

if day == int(day): # day가 정수라면
    print(int(day))
else: # day가 정수가 아니라면
    print(int(day)+1)

#import math
#print(math.ceil(day)) # 빠른 계산