import re

input = open("input.txt","r").read()

valid = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", input)

total = 0
enabled = True
for x in valid:
	match x[:3]:
		case "mul":
			if enabled:
				a,b = [int(x) for x in re.findall(r"\d+", x)]
				total += a*b
		case "do(":
			enabled = True
		case "don":
			enabled = False

print(total)