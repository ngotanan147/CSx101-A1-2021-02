a, b = [float(x) for x in input().split()]  

max = ((a+b) + abs(a-b))/2
min = ((a+b) - abs(a-b))/2

print("max = " + str(int(max)))
print("min = " + str(int(min)))
