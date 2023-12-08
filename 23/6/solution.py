import re, math

part = True

if part:
  file = [int(x) for x in re.findall("\d{1,10}", open("input.txt", "r+").read())]
  print(math.prod([sum([1 for x in range(time) if x*(time-x)>distance]) for time,distance in zip(file[:int(len(file)/2)], file[int(len(file)/2):])]))
else:
  time, distance = [int(x) for x in re.findall("\d{1,50}", open("input.txt", "r+").read().replace(" ", ""))]
  print(sum([1 for x in range(time) if x*(time-x) > distance]))