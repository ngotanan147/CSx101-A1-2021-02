q = int(input())

for i in range(q):
    n, k = map(int, input().split())
    lst = []
    lst = [int(x) for x in map(int, input().split())]
    print(lst.count(k))

# lst = [int(x) for x in map(int, input().split())]
# print(lst)
