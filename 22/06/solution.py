input = open("input.txt","r").read()


index = 0
while True:
  copies = False
  section = input[index:index+14]
  for x in section:
    if (y := section.index(x)) != section.rindex(x):
      copies = True
      index += y+1
      break
  if not copies:
    break
print(input.index(section))