n = input()

num = ['0', '1', '2', '3', '5', '6', '8', '9']


def isLuckyNum(n):
    lst = list(str(n))
    if '4' in lst:
        lst = list(filter(('4').__ne__, lst))
    if '7' in lst:
        lst = list(filter(('7').__ne__, lst))

    if len(lst) == 0:
        return True
    return False


def solve(n):
    s = list(n)
    count = 0
    count += s.count('4')
    count += s.count('7')
    if isLuckyNum(count):
        return 'YES'
    else:
        return 'NO'


print(solve(n))
