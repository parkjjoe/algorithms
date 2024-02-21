import sys

v = int(sys.stdin.readline())
vote = str(sys.stdin.readline())

if vote.count("A") > vote.count("B"):
    print("A")
elif vote.count("B") > vote.count("A"):
    print("B")
else:
    print("Tie")