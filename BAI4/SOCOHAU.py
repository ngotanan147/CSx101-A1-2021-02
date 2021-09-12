n, m = map(int, input().split())


def solve(n, m):
    if int(m) < 10 and int(n) <= int(m):
        return 1
    if int(m) < 10 and int(n) > int(m):
        return 0
    if n > m:
        return 0
    if n == m:
        return 1
    if len(str(n)) == len(str(m)):
        if int(n) > int(m):
            return 0
        else:
            return 1

    l = len(str(n))
    s = str(m)
    k = s[-l:]
    t = s[:len(s) - l]
    if int(n) <= int(k):
        return int(t) + 1
    return int(t)


a = solve(n, m)
print(a)
