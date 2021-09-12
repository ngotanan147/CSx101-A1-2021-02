

dic = {1:	'one',
       2:	'two',
       3:	'three',
       4:	'four',
       5:	'five',
       6:	'six',
       7:	'seven',
       8:	'eight',
       9:	'nine',
       10:  'ten',
       11:	'eleven',
       12:	'twelve',
       13:	'thirteen',
       14:	'fourteen',
       15:	'fifteen',
       16:	'sixteen',
       17:	'seventeen',
       18:	'eighteen',
       19:	'nineteen',
       20:	'twenty',
       30:	'thirty',
       40: 'forty',
       50: 'fifty',
       60: 'sixty',
       70: 'seventy',
       80: 'eighty',
       90: 'ninety'}


def dozen(n):
    if int(n) == 0:
        return ""
    if int(n) < 20:
        return dic[int(n)]

    a = int(str(n)[0] + str(0))
    b = int(str(n)[1:])

    if b != 0:
        return dic[a] + '-' + dic[b]
    else:
        return dic[a]


def hundred(n):
    if int(n) == 0:
        return ""
    a = int(str(n)[0])
    b = int(str(n)[1:])
    b = dozen(b)
    return dic[a] + " " + "hundred" + " " + b


def thousand(n):
    a = int(str(n)[0])
    b = int(str(n)[1:])
    if b < 100:
        b = dozen(b)
    else:
        b = hundred(b)
    if b == "":
        return dic[a] + " " + "thousand"
    else:
        return dic[a] + " " + "thousand," + " " + b


def solve(n):
    n = int(n)
    if n < 20:
        return dic[n]
    elif n < 100:
        return dozen(n)
    elif n < 1000:
        return hundred(n)
    else:
        return thousand(n)


n = int(input())

for i in range(n):
    a = int(input())
    print(solve(a))
