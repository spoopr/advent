input = open("input.txt","r").read()
floor = 0
for index, x in enumerate(input):
  if x == "(":
    floor += 1
  else:
    floor -= 1
  if floor < 0:
    print(index+1)
    break
print(floor)