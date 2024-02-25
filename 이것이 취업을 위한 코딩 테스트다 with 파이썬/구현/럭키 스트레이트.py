import sys

n = str(sys.stdin.readline().rstrip())

print("LUCKY" if sum(int(i) for i in n[:len(n) // 2]) == sum(int(i) for i in n[len(n) // 2:]) else "READY")
