import os
import numpy as np
import copy

os.chdir(os.getcwd()+r"\23\13")

part = False

if part:
  maps = open("input.txt", "r+").read().split("\n\n")
  asum = 0
  for _map in maps:
    start = asum
    _map = np.array([list(line) for line in _map.splitlines()])
    for i in range(1, len(_map)):
      if np.all(_map[i-min(i, len(_map)-i): i] == _map[i: i+min(i, len(_map)-i)][::-1]):
        asum += 100 * i
        break
    if start != asum:
      continue
    horizontal_map = np.rot90(_map, -1)
    for i in range(1, len(horizontal_map)):
      if np.all(horizontal_map[i-min(i, len(horizontal_map)-i): i] == horizontal_map[i: i+min(i, len(horizontal_map)-i)][::-1]):
        asum += i
        break
    if start != asum:
      continue
  print(asum)
else: 
  maps = open("input.txt", "r+").read().split("\n\n")
  asum = 0
  for _map in maps:
    start = asum
    _map = np.array([list(line) for line in _map.splitlines()])
    for i in range(1, len(_map)):
      if sum(np.concatenate(_map[i-min(i, len(_map)-i): i] == _map[i: i+min(i, len(_map)-i)][::-1])) == len(np.concatenate(_map[i-min(i, len(_map)-i): i]))-1:
        asum += 100 * i
        break
    if start != asum:
      continue
    horizontal_map = np.rot90(_map, -1)
    for i in range(1, len(horizontal_map)):
      if sum(np.concatenate(horizontal_map[i-min(i, len(horizontal_map)-i): i] == horizontal_map[i: i+min(i, len(horizontal_map)-i)][::-1])) == len(np.concatenate(horizontal_map[i-min(i, len(horizontal_map)-i): i]))-1:
        asum += i
        break
    if start != asum:
      continue
  print(asum)