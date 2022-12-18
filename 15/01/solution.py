input = open("input.txt","r").read()
floor = 0
for x in range(len(input)):
  match input[x]:
    case "(":
      floor +=1
    case ")":
      floor -=1
    if floor < 0:
      print(x+1)