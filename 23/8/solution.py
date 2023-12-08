import itertools, re, sys

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
  positions = [x for x in nodes.keys() if x[2] == "A"]
  finished = {}
  for node in nodes.keys():
    start = node
    for movement in instructions:
      if movement == "R":
        node = nodes[node][1]
      else:
        node = nodes[node][0]
    finished[start] = node
  asum = 0
  while not all(map(lambda x : x[2] == "Z", positions)):
    sys.stdout.write(str(asum))
    sys.stdout.flush()
    sys.stdout.write("\r")
    asum += len(instructions)
    newPositions = []
    for position in positions:
      newPositions.append(finished[position])
    positions = newPositions
  print(asum)