import numpy as np
import math

input = [a.splitlines() for a in open('input.txt',"r").read().split("\n\n")]

items = [eval("["+monkey[1].replace("  Starting items: ","")+"]") for monkey in input]

tests = [(int(monkey[3].replace("  Test: divisible by ","")), int(monkey[4].replace("    If true: throw to monkey ","")), int(monkey[5].replace("    If false: throw to monkey ",""))) for monkey in input]

operations = [monkey[2].replace('  Operation: new = ','').replace("old","item") for monkey in input]

_a = f"""
def operate(monkey, item):
  if monkey == 0:
    return {input[0][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 1:
    return {input[1][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 2:
    return {input[2][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 3:
    return {input[3][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 4:
    return {input[4][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 5:
    return {input[5][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 6:
    return {input[6][2].replace('  Operation: new = ','').replace("old","item")}
  elif monkey == 7:
    return {input[7][2].replace('  Operation: new = ','').replace("old","item")}
"""

exec(_a)

inspected = [0 for monkey in input]
big_mod = np.prod([int(monkey[3].split(" ")[-1]) for monkey in input])

for x in range(10000):
  print(x)
  for monkey, inventory in enumerate(items):
    for item in inventory:
      item = math.floor(operate(monkey, item)) % big_mod
      inspected[monkey] += 1
      if item % tests[monkey][0] == 0:
        items[tests[monkey][1]].append(item)
      else:
        items[tests[monkey][2]].append(item)
    items[monkey] = []

print(inspected)
print(items)
inspected.sort(reverse=True)

print(inspected[0]*inspected[1])