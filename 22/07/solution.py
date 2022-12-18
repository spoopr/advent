commandlist = [[y.split(" ") for y in x.splitlines()] for x in open("input.txt","r").read().split("$ ")] 
commandlist.pop(0)

filesystem = {"/":{}}
viewlist = []

#depackage

def get_from_list():
  a = filesystem
  for x in viewlist:
    a = a[x]
  return a
  
for command in  commandlist:
  if command[0][0] == "cd":
    if (y:= command[0][1]) != "..":
      viewlist.append(y)
    else: viewlist.pop()
  elif command[0][0] == "ls":
    command.pop(0)
    view = get_from_list()
    for x in command:
      if x[0] == "dir":
        view[x[1]] = {}
      else:
        view[x[1]] = int(x[0])

#find totals

def total(dict):
  bigtotal = 0
  dirs = []
  a = 0
  a_dict = {}
  for x in dict:
    if type(dict[x]) != type(1):
      y,x,z,_x = total(dict[x])
      bigtotal += z
      dirs.extend(_x)
      if x <= 100000:
        bigtotal += x
      if x >= 2536714:
        dirs.append(x)
    else:
      x = dict[x]
      y = x
    a_dict[x] = y
    a += x
  return a_dict,a, bigtotal, dirs

totaldict = total(filesystem)
totaldict[3].sort()
print(totaldict[3][0])