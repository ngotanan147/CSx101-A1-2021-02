from decimal import *
from math import *

psi = float(input())

kgscm = psi*(0.453592 / pow(2.54, 2))

getcontext().prec = 6

print(Decimal(kgscm).normalize())