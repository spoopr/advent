import re

input = open("input.txt","r").read()

valid = re.findall(r"mul\(\d+,\d+\)", input)

total = 0
for x in valid:
	a,b = [int(x) for x in re.findall(r"\d+", x)]
	total += a*b

print(total)