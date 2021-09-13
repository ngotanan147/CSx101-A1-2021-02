n = input()

characters = ["a", "o", "y", "e", "u", "i"]


def solve(n):
    n = str(n).lower()
    lst = list(str(n))
    lst2 = []
    for i in lst:
        if i not in characters:
            lst2.append(i)
    print('.' + '.'.join(lst2))


solve(n)
