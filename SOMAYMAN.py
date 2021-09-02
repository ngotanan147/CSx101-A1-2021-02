
n = input()

def checkLuckyNum(n):
    lst = list(str(n))
    lst = list(filter(('4').__ne__, lst))
    lst = list(filter(('7').__ne__, lst))
    if (len(lst) == 0):
        return True
    return False


def solve(n):
    lst = list(str(n))
    if (checkLuckyNum(n) == True):
        return "NO"
    if '4' in lst:
        return "YES"
    if '7' in lst:
        return "YES"
    return "NO"


print(solve(n))
