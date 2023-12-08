
part = False

if part:
  file = open("input.txt", "r+").read()
  x,y = (0,0)
  points = {(x,y)}
  key = {"^": (0,1), ">": (1,0), "v": (0,-1), "<": (-1,0)}
  for movement in file:
    x,y = [x + y for x,y in zip(key[movement], [x,y])]
    points.add((x,y))
  print(len(points))
else:
  file = open("input.txt", "r+").read()
  points = {(0,0)}
  key = {"^": (0,1), ">": (1,0), "v": (0,-1), "<": (-1,0)}
  for moveset in [file[::2], file[1::2]]:  
    x,y = (0,0)
    for movement in moveset:
      x,y = [x + y for x,y in zip(key[movement], [x,y])]
      points.add((x,y))
  print(len(points))