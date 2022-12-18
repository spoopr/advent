input = [int(x) for x in repr(open("input.txt","r").read()).replace("'","").replace(r"\n"," ").replace("-"," ").replace(","," ").split(" ")]
pairs = list(zip(input,input[1:],input[2:],input[3:]))[::4]
total = 0
between = lambda x,y,z : True if (x >= y and x <= z) else False
for x in pairs:
  if between(x[0],x[2],x[3]) or between(x[1],x[2],x[3]) or between(x[2], x[0], x[1]) or between(x[3],x[0],x[1]):
    total += 1
  else:
    print(x)