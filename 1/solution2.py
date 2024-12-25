import re

input = re.findall(r"\d+", open("input.txt", "r+").read())


left = [int(x) for x in input[::2]]
right = [int(x) for x in input[1::2]]

counting = {x:0 for x in right}
for x in right:
	counting[x] += 1

total = 0
for x in left:
	if x in right:
		total += x * counting[x]

print(total)
 