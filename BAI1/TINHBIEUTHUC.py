from math import *

a, b, c = [float(x) for x in input().split()]

x = pow(a, 5) - 2 * sqrt(abs(b)) + a*b*c

print(format(x, '.2f'))