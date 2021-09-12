import math
n, x = map(int, input().split())


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


a = divisorGenerator(x)
lst = []
for i in a:
    lst.append(int(i))


lst.reverse()
count = len(lst)

for i in range(len(lst) // 2 + 1):
    if lst[i] > n:
        count -= 2

if (count < 0):
    print(0)
else:
    print(count)
