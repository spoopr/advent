import re, math

part = False

if part:
  print(sum([int(re.findall("(?<=Game )\d{1,3}", line)[0]) for line in open("input.txt" , "r+").read().splitlines() if not any(map(lambda x,y : max(map(int, x)) > y, [re.findall("\d{1,2}(?= red)", line), re.findall("\d{1,2}(?= green)", line), re.findall("\d{1,2}(?= blue)",line)], [12,13,14]))]))
else:
  print(sum([math.prod(map(lambda x : max(map(int, x)), [re.findall("\d{1,2}(?= red)", line), re.findall("\d{1,2}(?= green)", line), re.findall("\d{1,2}(?= blue)", line)])) for line in open("input.txt" , "r+").read().splitlines()]))