import os, copy
import numpy as np
 
os.chdir(os.getcwd() + r"\23\21")

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  map = np.array([list(line) for line in file])

  start= np.where(map=="S")
  print(start)
  points = set()
  points.add((start[1][0], start[0][0]))    

  for i in range(6):
    pointsCopy = copy.copy(points)
    points.clear()
    for x,y in pointsCopy:
      for _x, _y in [(1,0),(-1,0),(0,1),(0,-1)]: 
        if map[y+_y, x+_x] in (".", "S") and not (x+_x, y+_y) in pointsCopy:
          points.add((x+_x, y+_y))
  print(len(points))
else:
  file = open("input.txt", "r+").read().splitlines()
  map = np.array([list(line) for line in file])

  start= np.where(map=="S")
  print(start)
  print(map.shape)
  points = set()
  points.add((start[1][0], start[0][0]))    

  for i in range(1000):
    pointsCopy = copy.copy(points)
    points.clear()
    for x,y in pointsCopy:
      for _x, _y in [(1,0),(-1,0),(0,1),(0,-1)]: 
        if map[(y+_y)%map.shape[0], (x+_x)%map.shape[1]] in (".", "S") and not (x+_x, y+_y) in pointsCopy:
          points.add((x+_x, y+_y))
  print(len(points))