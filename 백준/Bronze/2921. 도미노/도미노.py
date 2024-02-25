import sys

n = int(sys.stdin.readline())

up_sum = 0
down_sum = 0

for i in range(0,n+1):
    up = 0
    down = 0

    for j in range(0, i+1):
        up += j
        up_sum += up
        up = 0

    down += (i + 1) * i
    down_sum += down

print(up_sum + down_sum)