from math import *
# x + y = n
# 2x + 4y = legs

# 2 * (n - y) + 4y = legs
# y = (legs - 2n)/2

n, legs = [int(x) for x in input().split()]


def solve(n, legs):
    y = (legs - 2*n)/2
    x = n - y
    print(int(x), int(y))


solve(n, legs)  