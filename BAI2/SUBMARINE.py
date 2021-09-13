a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
k = int(input())
result = 0

if a[0] > a[1]:
    a[0], a[1] = a[1], a[0]
    b[0], b[1] = b[1], b[0]

EdgeHorizontal = b[0] == 1 or b[0] == a[0]
EdgeVertical = b[1] == 1 or b[1] == a[1]

if k == 1:
    result = 0
elif k == a[0] == a[1]:
    result = k
elif k == a[1]:
    result = k - 1
elif (EdgeHorizontal and EdgeVertical) or (k > a[0]):
    if EdgeVertical and (k > a[0]):
        result = k - 1
    else:
        result = k
else:
    if EdgeHorizontal or EdgeVertical:
        if EdgeHorizontal:
            if (b[1] - 1 < k - 1) or (a[1] - b[1] < k - 1):
                result += 1
            else:
                result += 2
        elif EdgeVertical:
            if (b[0] - 1 < k - 1) or (a[0] - b[0] < k - 1):
                result += 1
            else:
                result += 2
        result += (k-1)
    else:
        if ((b[1] - 1 >= k - 1) and (a[1] - b[1] >= k - 1)) and ((b[0] - 1 >= k - 1) and (a[0] - b[0] >= k - 1)):
            result += 2
        else:
            result += 1
        if k == a[0] and ((b[1] - 1 < k - 1) or (a[1] - b[1] < k - 1)):
            result += k - 1
        else:
            result += k

print(result)