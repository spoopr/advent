from operator import add,sub
import math

input = [[(y:=pair.split(" "))[0],int(y[1])] for pair in open("input.txt", "r").read().splitlines()]
rope_length = 10

direction_key = {
  "U" : (0,1),
  "D" : (0,-1),
  "L" : (-1,0),
  "R" : (1,0)
}

directions = {f"rope{x}":[] for x in range(rope_length+1)}
directions["rope0"] = [direction_key[pair[0]] for pair in input for x in range(pair[1])]

visited = {(0,0)}
finals = []
map_size = [0,0,0,0]

def move_closer(var):
  if var > 0:
    var -= 1
  else:
    var += 1
  return var

for rope_num in range(rope_length):
  current_rope = f"rope{rope_num}"
  next_rope = f"rope{rope_num+1}"
  rope_pos = [0,0]
  next_pos = [0,0]
  last_pos = [0,0]
  for move in directions[current_rope]:
    last_pos = rope_pos
    rope_pos = list(map(add,rope_pos,move))
    
    if rope_pos[0] < map_size[0]:
      map_size[0] = rope_pos[0]
    if rope_pos[1] < map_size[1]:
      map_size[1] = rope_pos[1]
    if rope_pos[0] > map_size[2]:
      map_size[2] = rope_pos[0]
    if rope_pos[1] > map_size[3]:
      map_size[3] = rope_pos[1]
      
    if (distance := math.dist(rope_pos,next_pos)) >= 2:

      next_move = list(map(sub,rope_pos,next_pos))
      if next_move[0] == next_move[1]:
        next_move[0] = move_closer(next_move[0])
        next_move[1] = move_closer(next_move[1])
      elif abs(next_move[0]) > abs(next_move[1]):
        next_move[0] = move_closer(next_move[0])
      else:
        next_move[1] = move_closer(next_move[1])

      directions[next_rope].append(next_move)
      next_pos = list(map(add,next_pos,next_move))

    #if rope_num == 8:
      #finals.append(next_pos)
    
    if next_rope == f'rope{rope_length-1}':
      visited.add(tuple(next_pos))
      
  finals.append(rope_pos)
  

array = [["-" for y in range(1+map_size[2]-map_size[0])]for x in range(1+map_size[3]-map_size[1])]

finals.insert(0,[0,0])

for pos in range(len(finals)):
  ypos =   finals[pos][1] - map_size[1]
  xpos = finals[pos][0] - map_size[0]
  array[ypos][xpos] = str(pos) if pos != 0 else "s"

a = ["".join(x) for x in array]
a.reverse()
print("\n".join(a))
#print(visited)
print(len(visited))