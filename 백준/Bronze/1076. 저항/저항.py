import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
third = sys.stdin.readline().rstrip()

color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

print((10 * color.index(first) + color.index(second)) * (10 ** color.index(third)))