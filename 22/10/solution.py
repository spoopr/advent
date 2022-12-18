input =  open("input.txt", "r").read().replace("addx ","noop\n").splitlines()
adds = []
for x in range(len(input)):
  if input[x] == "noop":
    adds.append(0)
  else:
    if len(adds) == x:
      adds.append(0)
    adds.append(int(input[x]))
x = 1
x_values = []
for y in adds:
  x += y
  x_values.append(x)

a = lambda index : index*40 + 19
signals = [x_values[a(x)]*(a(x)+1) for x in range(6)]

pixels = []
for x in range(240):
  if abs(x_values[x] - (x%40)) <= 1:
    pixels.append("#")
  else: pixels.append("-")
  if (x+1)%40 == 0:
    pixels[-1] += "\n"

pixels = "".join(pixels)
print(pixels)