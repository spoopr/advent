import os
import numpy as np

part = False

os.chdir(os.getcwd()+r"\23\10")

if part:
  file = open("input.txt", "r+").read().splitlines()
  maze = np.array([list(x) for x in file])
  valueMaze = np.full_like(maze, -1, dtype=int)
  y,x = np.where(maze=="S")
  print(x[0],y[0])
  visited = set()
  activePoints = {(x[0],y[0])}
  nextPoints = set()
  movesKey = {"S": {(1,0), (-1,0), (0,1), (0,-1)},"|":{(0,1),(0,-1)},"-":{(1,0),(-1,0)},"L":{(0,-1),(1,0)},"J":{(0,-1),(-1,0)},"7":{(0,1),(-1,0)},"F":{(0,1),(1,0)}}
  iteration = 0
  while activePoints:
    for x, y in activePoints:
      valueMaze[y,x] = iteration
      visited.add((x,y))
      for moveX, moveY in movesKey[maze[y,x]]:
        if (-1*moveX, -1*moveY) in movesKey.get(maze[y+moveY, x+moveX], []):
          nextPoints.add((x+moveX, y+moveY))
    iteration += 1
    activePoints.clear()
    activePoints.update(nextPoints.difference(visited))
    nextPoints.clear()
  print(np.max(valueMaze))
else:
  file = open("input.txt", "r+").read().splitlines()
  maze = np.array([list(x) for x in file])
  valueMaze = np.full_like(maze, -2, dtype=int)
  y,x = np.where(maze=="S")
  visited = {(x[0],y[0])}
  activePoints = {((x[0]+1, y[0]),(1,0)),((x[0],y[0]-1),(1,0))}
  nextPoints = set()
  movesKey = {"S": {(1,0), (-1,0), (0,1), (0,-1)},"|":{(0,1),(0,-1)},"-":{(1,0),(-1,0)},"L":{(0,-1),(1,0)},"J":{(0,-1),(-1,0)},"7":{(0,1),(-1,0)},"F":{(0,1),(1,0)}}
  rotationKey = {"L":{(1,0):(0,-1), (-1,0):(0,1), (0,1):(-1,0), (0,-1):(1,0)},"J":{(1,0):(0,1), (-1,0):(0,-1), (0,1):(1,0), (0,-1):(-1,0)},"7":{(1,0):(0,-1), (-1,0):(0,1), (0,1):(-1,0), (0,-1):(1,0)},"F":{(1,0):(0,1), (-1,0):(0,-1), (0,1):(1,0), (0,-1):(-1,0)}}
  valueMaze[y[0],x[0]] = 0
  while activePoints:
    for position, offset in activePoints:
      print("\n")
      print(valueMaze)
      print(position, offset, maze[*position[::-1]])
      x,y = position
      offX, offY = offset
      visited.add((x,y))
      valueMaze[y,x] = 0
      if 0 <= x+offX < len(maze[0]) and 0 <= y+offY < len(maze):
        if maze[y+offY, x+offX] == ".":
          valueMaze[y+offY, x+offX] = 1
      for moveX, moveY in movesKey[maze[y,x]]:
        if (-1*moveX, -1*moveY) in movesKey.get(maze[y+moveY, x+moveX], []):
          if 0 <= x+offX+moveX < len(maze[0]) and 0 <= y+offY+moveY < len(maze):
            if maze[y+offY+moveY, x+offX+moveX] == "." and (moveX, moveY) != offset:
              valueMaze[y+offY+moveY, x+offX+moveX] = 1
          nextPoints.add(((x+moveX, y+moveY), rotationKey[maze[y+moveY, x+moveX]][offset] if maze[y+moveY, x+moveX] in rotationKey.keys() else offset))
    activePoints.clear()
    activePoints.update((position, offset) for position, offset in nextPoints if not position in visited)
    nextPoints.clear()
  outsidePoints = set(zip(*reversed(np.where(valueMaze==1))))
  print(valueMaze)
  while outsidePoints:
    x,y = outsidePoints.pop()
    for moveX, moveY in [(1,0),(-1,0),(0,1),(0,-1)]:
      try:
        if not valueMaze[y+moveY, x+moveX] in [0,1]:
          outsidePoints.add((x+moveX, y+moveY))
          valueMaze[y+moveY, x+moveX] = 1
      except IndexError:
        pass

  print(maze)
  print(valueMaze)
  print(len(valueMaze[np.isin(valueMaze,[-2])]))
  print(len(valueMaze[np.isin(valueMaze,[1])]))