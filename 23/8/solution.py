import itertools, re
import numpy as np

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  instructions = list(file[0])
  nodes = {line.split(" = ")[0]: list(re.findall("[A-Z]{3}", line.split(" = ")[1])) for line in file[2:]}
  position = "AAA"
  asum = 0
  while position != "ZZZ":
    asum += len(instructions)
    for movement in instructions:
      if movement == "R":
        position = nodes[position][1]
      else:
        position = nodes[position][0]
  print(asum)
else:
  file = open("input.txt", "r+").read().splitlines()
  instructions = list(file[0])
  nodes = {line.split(" = ")[0]: list(re.findall("[A-Z\d]{3}", line.split(" = ")[1])) for line in file[2:]}
  finished = {}
  for node in nodes.keys():
    start = node
    for movement in instructions:
      if movement == "R":
        node = nodes[node][1]
      else:
        node = nodes[node][0]
    finished[start] = node
  loop = []
  for node in finished.keys():
    if node[2] == "Z":
      asum = 1
      start = node
      node = finished[node]
      while node[2] != "Z":
        asum += 1
        node = finished[node]
      loop.append(asum)
  print(np.lcm.reduce(loop) * len(instructions))