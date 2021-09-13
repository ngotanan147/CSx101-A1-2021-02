
n = int(input())


def solve(n):
    lst = list(str(n))
    k = len(lst)
    sum = 0
    for i in lst:
        sum += int(i)**int(k)
    if sum == n:
        print(True)
    else: print(False)


solve(n)