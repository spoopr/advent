from operator import add
import copy

part = False

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
  oxygen = copy.copy(file)
  carbon = copy.copy(file)
  for index in range(len(file[0])):
    sum = 0
    for line in oxygen:
      sum += int(line[index])
    if len(oxygen) > 1:
      oxygen = [line for line in oxygen if int(line[index]) == round(sum/len(oxygen)+0.00001)]
    sum = 0
    for line in carbon:
      sum += int(line[index])
    if len(carbon) > 1:
      carbon = [line for line in carbon if int(line[index]) != round(sum/len(carbon)+0.00001)]
  print(carbon)
  print(oxygen)
  print(int(oxygen[0], 2) * int(carbon[0], 2))