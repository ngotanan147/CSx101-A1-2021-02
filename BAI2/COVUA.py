import math
n = int(input())
x, y = map(int, input().split())


def findDistance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p2[1] - p1[1]))


def solve(n, x, y):
    if x == 1 and y == 1:
        print('White')
        return
    if x == n and y == n:
        print('Black')
        return
        
    blackPoint = [n, n]
    whitePoint = [1, 1]
    d1 = findDistance(whitePoint, [x, y])
    d2 = findDistance(blackPoint, [x, y])
    if d1 > d2:
        print('Black')
    else:
        print('White')


solve(n, x, y)
