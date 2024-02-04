# -*- coding: utf-8 -*-
import sys

s = str(sys.stdin.readline().rstrip())
c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


for i in c:
    s = s.replace(i, "0")

print(len(s))