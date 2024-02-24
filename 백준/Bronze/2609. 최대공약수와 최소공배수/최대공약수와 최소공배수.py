import sys
from math import lcm, gcd

a, b = map(int, sys.stdin.readline().split())

print(f"""{gcd(a, b)}
{lcm(a, b)}""")