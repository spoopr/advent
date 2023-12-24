import os, sys
import numpy as np

os.chdir(os.getcwd()+r"/23/18")

part = True

if part:
  file = open("input.txt").read().splitlines()
  visited = set()
  visited.add((0,0))
  pos = np.array([0,0])
  key = {"R": np.array([1,0]), "L": np.array([-1,0]), "U": np.array([0,-1]), "D": np.array([0,1])}
  for line in file:
    command, value, color = line.split(" ")
    for _ in range(int(value)):
      pos += key[command]
      visited.add(tuple(pos))
  xValues = [x for x,y in visited]
  yValues = [y for x,y in visited]
  display = np.full((max(yValues)+1-min(yValues), max(xValues)+1-min(xValues)), ".")
  for x, y in visited:
    display[y+min(yValues), x+min(xValues)] = 1
  points = set()
  points.add((1,1))
  while points:
    x,y = points.pop()
    visited.add((x,y))
    display[y+min(yValues),x+min(xValues)] = 1
    for _x, _y in [(1,0),(-1,0),(0,1),(0,-1)]:
      if not (x+_x, y+_y) in visited:
        points.add((x+_x,y+_y))
  print(len(visited))