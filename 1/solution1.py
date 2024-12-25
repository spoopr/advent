import re

input = re.findall(r"\d+", open("input.txt", "r+").read())


a = sorted([int(x) for x in input[::2]])
b = sorted([int(x) for x in input[1::2]])


sum = 0

for x,y in zip(a,b):
	sum += abs(x-y)

print(sum)
