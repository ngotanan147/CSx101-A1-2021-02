tre_trung, xinh_dep, co_gau, giau_co = map(int, input().split())

chanLi = ['true', 'true', 'true']


def solve(tre_trung, xinh_dep, co_gau, giau_co):
    if xinh_dep and tre_trung == 0:
        chanLi[0] = 'false'
    if co_gau and xinh_dep == 0:
        chanLi[1] = 'f  lse'
    if xinh_dep == 0 and co_gau and giau_co == 0:
        chanLi[2] = 'false'
    if chanLi.count('true') == 3:
        print(1)
    else:
        print(0)


solve(tre_trung, xinh_dep, co_gau, giau_co)
