import os
import numpy as np

os.chdir(os.getcwd()+r"\23\14")

part = True

if part:
  rockMap = np.array([list(line) for line in open("input.txt","r+").read().splitlines()])
  asum = 0
  for y,x in zip(*np.where(rockMap=="O")):
    if "#" in rockMap[:y, x]:
      nearestImmovableY = np.where(rockMap[:y,x]=="#")[0][-1]
      asum += (len(rockMap)) - (nearestImmovableY + sum(rockMap[nearestImmovableY:y,x]=="O") + 1)
    else:
      asum += (len(rockMap)) - sum(rockMap[:y,x]=="O")
  print(asum)
