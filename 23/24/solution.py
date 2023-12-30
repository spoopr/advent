import os, re, itertools
import numpy as np

os.chdir(os.getcwd() + r"/23/24")

part = True

if part:
  hailstones = [np.fromiter(re.findall(r"[-]?\d+", line), dtype=np.int64) for line in open("input.txt", "r+").read().splitlines()] 
  asum = 0
  for path1, path2 in itertools.combinations(hailstones, 2):
    ax, ay, az, aVx, aVy, aVz = path1
    bx, by, bz, bVx, bVy, bVz = path2

    if ((aVx/aVy)-(bVx/bVy)) == 0 or ((aVy/aVx)-(bVy/bVx)) == 0:
      continue

    x,y = (
      ((((-1*bVy/bVx)*bx)+ by) - (((-1*aVy/aVx)*ax)+ay)) / ((aVy/aVx)-(bVy/bVx)),
      ((((-1*bVx/bVy)*by) + bx) - (((-1*aVx/aVy)*ay) +ax))/ ((aVx/aVy)-(bVx/bVy))
    )

    quadrants = {
      (False, False): (x >= ax and y >= ay, x >= bx and y >= by),
      (True, False): (x <= ax and y >= ay, x <= bx and y >= by),
      (True, True): (x <= ax and y <= ay, x <= bx and y <= by),
      (False, True): (x >= ax and y <= ay, x >= bx and y <= by)
      }

    start = 200000000000000
    end = 400000000000000
    if quadrants[(aVx < 0, aVy < 0)][0] and quadrants[(bVx < 0, bVy < 0)][1] and start <= x <= end and start <= y <= end:
      asum += 1 
  print(asum)