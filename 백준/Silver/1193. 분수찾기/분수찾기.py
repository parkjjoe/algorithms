import sys

n = int(sys.stdin.readline())
line = 1

# line 1: 1/1
# line 2: 1/2 2/1
# line 3: 3/1 2/2 1/3
# ...
while n > line: # n이 어느 line의 몇 번째에 있는지 확인
    n -= line
    line += 1

if line % 2 == 0: # 짝수 line은 분자 1씩 증가, 분모 1씩 감소
    up = n
    down = line - n + 1
else: # 홀수 line은 분자 1씩 감소, 분모 1씩 증가
    up = line - n + 1
    down = n

print(str(up) + "/" + str(down))