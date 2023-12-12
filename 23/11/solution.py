import numpy as np
import itertools

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  galaxyMap = np.array([list(x) for x in file])
  galaxyMap = np.insert(galaxyMap, np.arange(len(galaxyMap))[np.all(galaxyMap==".", axis=1)], "."*len(galaxyMap[0]), axis=0)
  galaxyMap = np.insert(galaxyMap.T, np.arange(len(galaxyMap[0]))[np.all(galaxyMap.T==".", axis=1)], "."*len(galaxyMap), axis=0).T
  galaxyCoords = list(zip(*reversed(np.where(galaxyMap=="#"))))
  print(galaxyMap)
  print(galaxyCoords)
  asum = 0
  for coord1, coord2 in itertools.combinations(galaxyCoords, 2):
    asum += abs(coord1[0]-coord2[0])
    asum += abs(coord1[1]-coord2[1])
  print(asum)
else:
  file = open("input.txt", "r+").read().splitlines()
  galaxyMap = np.array([list(x) for x in file])
  galaxyCoords = list(zip(*reversed(np.where(galaxyMap=="#"))))
  asum = 0
  for coord1, coord2 in itertools.combinations(galaxyCoords, 2):
    asum += abs(coord1[0]-coord2[0])
    asum += abs(coord1[1]-coord2[1])
    emptyRows = len(galaxyMap[min(coord1[1], coord2[1]) : max(coord1[1], coord2[1])][np.all(galaxyMap[min(coord1[1], coord2[1]) : max(coord1[1], coord2[1])]==".", axis=1)])
    asum += 1000000 * emptyRows
    asum -= emptyRows
    emptyColumns = len(galaxyMap.T[min(coord1[0],coord2[0]) : max(coord1[0],coord2[0])][np.all(galaxyMap.T[min(coord1[0],coord2[0]) : max(coord1[0],coord2[0])]==".", axis=1)])
    asum += 1000000 * emptyColumns
    asum -= emptyColumns
  print(asum)