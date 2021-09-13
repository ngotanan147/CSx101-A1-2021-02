n = int(input())

can = ['GIAP', 'AT', 'BINH', 'DINH', 'MAU', 'KY', 'CANH', 'TAN', 'NHAM', 'QUY']
giap = ["TY'", 'SUU', 'DAN', 'MEO', 'THIN', 'TY.',
        'NGO', 'MUI', 'THAN', 'DAU', 'TUAT', 'HOI']


def solve(y):
    canIndex = 0
    giapIndex = 0
    if y > 0:
        if y == 1:
            print('TAN DAU')
            return
        else:
            canIndex = (y + can.index('TAN')) % 10 - 1
            giapIndex = (y + giap.index('DAU')) % 12 - 1
    if y < 0:
        can.reverse()
        giap.reverse()
        if y == -1:
            print('CANH THAN')
            return
        else:
            canIndex = (abs(y) + can.index('CANH')) % 10 - 1
            giapIndex = (abs(y) + giap.index('THAN')) % 12 - 1

    print(can[canIndex], giap[giapIndex])


solve(n)

