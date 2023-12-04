from operator import add

part = True

if part:
  file = open("input.txt", "r+").read().splitlines()
  _sum = [0] * len(file[0])
  for line in file:
    _sum = map(add, _sum, map(int, list(line)))
  _sum = [round(x/len(file)) for x in _sum]
  gamma = int("".join(map(str, _sum)),2)
  epsilon = int("".join(map(lambda x : str(int(not(x))), _sum)),2)
  print(gamma * epsilon)
else:
  file = open("input.txt", "r+").read().splitlines()
  