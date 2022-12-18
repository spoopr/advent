crates, moves = repr(open("input.txt","r").read()).replace("'","").split(r"\n\n")

crates = crates.split(r"\n")
crates.pop()
moves = moves.split(r"\n")

#depackage 

stacks = [[crate for y in range(len(crates)) if (crate:= crates[y][4*x + 1]) != " "]for x in range(int((len(crates[0])+1)/4))]
for x in stacks: x.reverse()

moves = [[int(y) for y in x.replace("move ","").replace("from ","").replace("to ","").split(" ")] for x in moves]

#move
for moveset in moves:
  moving = stacks[moveset[1]-1][-1*moveset[0]:]
  #moving.reverse()
  stacks[moveset[1]-1] = stacks[moveset[1]-1][:-1*moveset[0]]
  stacks[moveset[2]-1].extend(moving)

a = ""
for x in stacks:
  a += x[-1]

print(a)