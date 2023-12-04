
part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  depth = 0
  distance = 0
  for line in file:
    action, value = line.split(" ")
    value = int(value)
    if action == "forward":
        distance += value
    elif action == "down":
      depth += value
    elif action == "up":
      depth -= value
  print(depth*distance)
else:
  file = open("input.txt", "r+").read().splitlines()
  depth = 0
  aim = 0
  distance = 0
  for line in file:
    action, value = line.split(" ")
    value = int(value)
    if action == "forward":
      distance += value
      depth += aim*value
    elif action == "down":
      aim += value
    elif action == "up":
      aim -= value 
  print(depth*distance)