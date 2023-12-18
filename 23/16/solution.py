import os 
import numpy as np

os.chdir(os.getcwd()+r"\23\16")

part = False

if part:
  mirrorMap = np.array([list(line) for line in open("input.txt", "r+").read().splitlines()])
  beams = set()
  beams.add(((0,0),(1,0)))
  visited = set() 
    
  while beams:
    position, direction = beams.pop()
    visited.add((position, direction)) 
    for new in {".": lambda x: [x], "|": lambda x: [(0,1),(0,-1)] if x[0] else [x], "-": lambda x: [(1,0),(-1,0)] if x[1] else [x], "/": lambda x : [tuple(-1*y for  y in x[::-1])], "\\": lambda x: [tuple(y for y in x[::-1])]}[mirrorMap[position[1], position[0]]](direction):
      newPosition = (position[0] + new[0], position[1] + new[1])
      if (not (newPosition, new) in visited) and 0 <= newPosition[0] < len(mirrorMap) and 0 <= newPosition[1] < len(mirrorMap):
        beams.add((newPosition, new))
  print(len(set(x for x,y in visited)))

else:
  mirrorMap = np.array([list(line) for line in open("input.txt", "r+").read().splitlines()])

  def check(position, direction):
    beams = set()
    beams.add((position,direction))
    visited = set()  

    while beams:
      position, direction = beams.pop()
      visited.add((position, direction))
      for new in {".": lambda x: [x], "|": lambda x: [(0,1),(0,-1)] if x[0] else [x], "-": lambda x: [(1,0),(-1,0)] if x[1] else [x], "/": lambda x : [tuple(-1*y for  y in x[::-1])], "\\": lambda x: [tuple(y for y in x[::-1])]}[mirrorMap[position[1], position[0]]](direction):
        newPosition = (position[0] + new[0], position[1] + new[1])
        if (not (newPosition, new) in visited) and 0 <= newPosition[0] < len(mirrorMap) and 0 <= newPosition[1] < len(mirrorMap):
          beams.add((newPosition, new))
    return len(set(x for x,y in visited))
  print(max([check((x,0),(0,1)) for x in range(len(mirrorMap[0]))] + [check((x,len(mirrorMap)-1),(0,-1)) for x in range(len(mirrorMap[0]))] + [check((0,y),(1,0)) for y in range(len(mirrorMap))] + [check((len(mirrorMap[0])-1, y),(-1,0)) for y in range(len(mirrorMap))]))