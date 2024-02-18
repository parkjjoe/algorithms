def solution(sides):
    sides.sort()
    return 1 if int(sides[2]) < int(sides[0]) + int(sides[1]) else 2