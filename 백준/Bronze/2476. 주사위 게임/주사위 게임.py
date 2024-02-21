import sys

n = int(sys.stdin.readline())

money = []

for _ in range(n):
    eye = list(map(int, sys.stdin.readline().split()))

    if eye[0] == eye[1] == eye[2]:
        money.append(10000 + eye[0] * 1000)
    elif eye[0] == eye[1] or eye[0] == eye[2]:
        money.append(1000 + eye[0] * 100)
    elif eye[1] == eye[2]:
        money.append(1000 + eye[1] * 100)
    elif eye[0] != eye[1] and eye[1] != eye[2] and eye[2] != eye[0]:
        money.append(max(eye) * 100)

print(max(money))