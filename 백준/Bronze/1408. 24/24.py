import sys

h1, m1, s1 = map(int, sys.stdin.readline().split(":"))
h2, m2, s2 = map(int, sys.stdin.readline().split(":"))

time = (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1)

if time < 0:
    time += 3600 * 24

print("%02d:%02d:%02d" % (time // 3600, time % 3600 // 60, time % 60))