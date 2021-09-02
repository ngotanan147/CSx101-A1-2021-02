
n = int(input())


def Fibonacci(n):
    if (n == 0):
        print(0)
        return
    preNum = 0
    num = 1
    t = 0
    for _ in range(n - 1):
        t = preNum
        preNum = num
        num = num + t
    print(num)

Fibonacci(n)
