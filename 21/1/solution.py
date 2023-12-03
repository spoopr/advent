
part = False
if part:
  file = open("input.txt", "r+").read().splitlines()
  sum = 0
  last = 1000000
  for line in file:
    line = int(line)
    if line > last:
      sum += 1
    last = line
  print(sum)
else:
  file = open("input.txt", "r+").read().splitlines()
  _sum = 0
  triSet = [1000000,int(file[0]),int(file[1])]
  for line in file[2:]:
    lastSum = sum(triSet)
    triSet.pop(0)
    triSet.append(int(line))
    if sum(triSet) > lastSum:
      _sum += 1
  print(_sum)