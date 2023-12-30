import os
import numpy as np
import copy
import sys

os.chdir(os.getcwd() + r"/23/23")

part = False

if part:
  map = np.array([list(x) for x in open("input.txt", "r+").read().splitlines()])
  end = (map.shape[1]-2, map.shape[0]-1)

  invalidKey = {">": (-1, 0), "<": (1,0), "v": (0, -1), "^": (0,1), ".": (0,0)}

  def long(x,y):
    asum = 0
    history = set()
    while True:
      history.add((x,y))
      if (x,y) == end:
        return asum
      available = [pair for pair in ((1,0),(-1,0),(0,1),(0,-1)) if (not (x+pair[0], y+pair[1]) in history) and map[y+pair[1], x+pair[0]] != "#" and pair != invalidKey[map[y+pair[1], x+pair[0]]]]  
      asum += 1
      if len(available) > 1:
        return asum + 1 + max([long(x+(pair[0]*2), y+(pair[1]*2)) for pair in available])
      else:
        _x, _y = available[0]
        x += _x
        y += _y

  print(long(1,0))

else:
  map = np.array([list(x) for x in open("input.txt", "r+").read().splitlines()])
  end = (map.shape[1]-2, map.shape[0]-1)

  global a
  a = 0

  def long(x,y, history=set()):
    global a
    asum = 0
    while True:
      a += 1
      sys.stdout.write(f"\r{str(a)}")
      sys.stdout.flush()
      history.add((x,y))
      if (x,y) == end:
        return asum
      available = [pair for pair in ((1,0),(-1,0),(0,1),(0,-1)) if (not (x+pair[0], y+pair[1]) in history) and map[y+pair[1], x+pair[0]] != "#"]  
      if len(available) == 0:
        return 0
      asum += 1
      if len(available) > 1:
        return asum + max([long(x+(pair[0]), y+(pair[1]), copy.copy(history)) for pair in available])
      else:
        _x, _y = available[0]
        x += _x
        y += _y

  print("\n", long(1,0))

