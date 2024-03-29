import sys

agent = [str(sys.stdin.readline().rstrip()) for _ in range(5)]
flag = False

for i in agent:
    if "FBI" in i:
        print(agent.index(i) + 1, end=" ")
        flag = True

if not flag:
    print("HE GOT AWAY!")