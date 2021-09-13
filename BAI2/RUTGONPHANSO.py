from fractions import Fraction as F

n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))


def solve(lst):
    for item in lst:
        kq = F(item[0], item[1])
        kq = str(kq).split('/')
        if (len(kq) == 1):
            print(kq[0])
        else:
            print(kq[0], kq[1])


solve(lst)
