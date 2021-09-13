from decimal import *

f = float(input())

c = (f-32)/1.8
k = c+273.15

getcontext().prec = 6

print(Decimal(c).normalize(), Decimal(k).normalize())