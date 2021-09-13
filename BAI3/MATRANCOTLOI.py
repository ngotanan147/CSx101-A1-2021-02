

for r_idx in range(5):
  row = map(int, input().split()) 
  for c_idx in range(5):
    if row[c_idx] == 1:
      numSteps = abs(r_idx - 2) + abs(c_idx - 2)
      print(numSteps)
      break