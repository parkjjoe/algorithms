import sys

while 1:
    n = int(sys.stdin.readline())
    list = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            list.append(i)

    if n == sum(list):
        print(f"{n} =", " + ".join(str(i) for i in list))
    else:
        print(f"{n} is NOT perfect.")