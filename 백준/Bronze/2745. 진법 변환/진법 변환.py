import sys

n, b = map(str, sys.stdin.readline().rstrip().split())

print(int(n, int(b)))

# 더 복잡한 코드
# 
# n, b = map(str, sys.stdin.readline().rstrip().split())
# array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# n = n[::-1] # 진법 계산을 위한 역순 처리
# answer = 0
# 
# for i in range(len(n)):
#     answer += (i ** int(b)) * (array.index(n[i])) # ex. 0^36 * Z + 1^36 * Z + ...
# 
# print(answer)