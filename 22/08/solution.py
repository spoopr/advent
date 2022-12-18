horizontal_map = [[int(x) for x in y] for y in open("input.txt","r").read().splitlines()]
vertical_map = [[horizontal_map[y][x] for y in range(len(horizontal_map))] for x in range(len(horizontal_map[0]))]

visible = 0 

scene_map = []

def distance(trees, height):
  if trees == []:
    return 1
  else:
    for x in range(len(trees)):
      if trees[x] >= height:
        return x+1
    return len(trees)

for y in range(len(horizontal_map)):
  for x in range(len(horizontal_map[0])):

    value = horizontal_map[y][x] 
    horizontal = (horizontal_map[y][:x].copy(),horizontal_map[y][x+1:].copy())
    vertical = (vertical_map[x][:y].copy(), vertical_map[x][y+1:].copy())

    horizontal[0].reverse()
    vertical[0].reverse()
    
    scene_map.append(distance(horizontal[0],value)* distance(horizontal[1],value)* distance(vertical[0],value)* distance(vertical[1],value))

    
    
    if (x == 0) or (y == 0) or (y == len(horizontal_map)-1) or (x == len(vertical_map)-1):
      visible += 1
    else:
      horizontal[0].sort(reverse=True)
      horizontal[1].sort(reverse=True)
      vertical[0].sort(reverse=True)
      vertical[1].sort(reverse=True)
      
      if (horizontal[0][0] < value) or (horizontal[1][0] < value) or (vertical[0][0] < value) or (vertical[1][0] < value):
        visible += 1

scene_map.sort()