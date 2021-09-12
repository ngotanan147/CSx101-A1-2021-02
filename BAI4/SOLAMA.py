
def donVi(n):
    if n == 0:
        return ''
    if n < 5 and n != 4:
        return n * 'I'
    if n == 4:
        return 'IV'
    if n < 10 and n != 9:
        return 'V' + (n - 5) * 'I'
    if n == 9:
        return 'IX'
    return 'X'


def hangChuc(n):
    if n == 0:
        return ''
    if len(str(n)) == 1:
        b = 0
    else:
        b = int(str(n)[1])
    a = int(str(n)[0])
    if n < 50 and a != 4:
        return a * 'X' + donVi(b)
    if a == 4:
        return 'XL' + donVi(b)
    if n < 100 and a != 9:
        return 'L' + (a - 5) * 'X' + donVi(b)
    if a == 9:
        return 'XC' + donVi(b)
    return 'C'


def hangTram(n):
    if n == 0:
        return ''
    if len(str(n)) == 1:
        b = c = 0
    elif len(str(n)) == 2:
        c = 0
        b = b = int(str(n)[1])
    else:
        b = int(str(n)[1])
        c = int(str(n)[2])

    a = int(str(n)[0])

    if a == 0 and b == 0 and c == 0:
        return
    if n < 500 and a != 4:
        return a * 'C' + hangChuc(b * 10) + donVi(c)
    if a == 4:
        return 'CD' + hangChuc(b * 10) + donVi(c)
    if n < 1000 and a != 9:
        return 'D' + (a - 5) * 'C' + hangChuc(b * 10) + donVi(c)
    if a == 9:
        return 'CM' + hangChuc(b * 10) + donVi(c)
    return 'M'


def solve(n):
    if n <= 10:
        return donVi(n)
    if n <= 100:
        return hangChuc(n)
    if n <= 1000:
        return hangTram(n)
    a = int(str(n)[0])
    b = int(str(n)[1])
    c = int(str(n)[2])
    d = int(str(n)[3])
    return a * 'M' + hangTram(b * 100) + hangChuc(c * 10) + donVi(d)


n = int(input())
for i in range(n):
    a = int(input())
    print(solve(a))
