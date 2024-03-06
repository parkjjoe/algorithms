import sys

n, c = map(int, sys.stdin.readline().split())

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()

start = 1 # 최소 gap
end = array[-1] - array[0] # 최대 gap
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, n): # 앞에서부터 공유기 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c: # 공유기를 c개 이상 설치할 수 있으면 거리 증가
        start = mid + 1
        result = mid
    else: # 공유기를 c개 이상 설치할 수 없으면 거리 감소
        end = mid - 1

print(result)
