import numpy as np
import re
import math

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  asum = 0
  for line in file:
    nums = [int(x) for x in re.findall("\d{1,2}", line)]
    asum += 2 * sum(map(math.prod, zip(nums, np.roll(nums,1))))
    asum += math.prod(sorted(nums)[:2])
  print(asum)
else:
  file = open("input.txt", "r+").read().splitlines()
  asum = 0
  for line in file:
    nums = [int(x) for x in re.findall("\d{1,2}", line)]
    asum += math.prod(nums)
    asum += sum(sorted(nums)[:2])*2
  print(asum)
