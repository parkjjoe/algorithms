import sys

n = int(sys.stdin.readline())

bee = 1
count = 1

while n > bee: # n번 방이 bee 방 번호보다 크면 반복
    bee += 6 * count # 가운데를 둘러싼 방의 개수가 6의 배수로 증가함.
    count += 1 # 둘레를 하나 벗어날 때마다 count 1 증가
    
print(count)