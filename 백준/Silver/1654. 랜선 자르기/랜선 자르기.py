import sys

k, n = map(int, sys.stdin.readline().split())

ran = []

for _ in range(k):
    ran.append(int(sys.stdin.readline()))

start, end = 1, max(ran) # 잘릴 랜선 길이

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in ran:
        count += i // mid # 랜선을 mid로 잘랐을 때, 잘린 랜선의 개수

    if count >= n: # n개 이상을 만들 수 있다면 mid + 1부터 end까지 탐색
        start = mid + 1
    else: # n개 미만으로 만들어지면 start부터 mid - 1까지 탐색
        end = mid - 1

print(end) # while문을 벗어났을 때 end 값이 가장 긴 랜선의 길이