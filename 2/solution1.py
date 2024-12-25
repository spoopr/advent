import re

input = open("input.txt", "r+").read().splitlines()

totalUnsafe = 0
for line in input:
	numbers = [int(x) for x in re.findall(r"\d+", line)]
	increasing = numbers[0] < numbers[1]
	for a,b in zip(numbers, numbers[1:]):
		if not ((1 <= abs(a - b) <= 3) and ((a < b) == increasing)):
			totalUnsafe += 1
			break

print(len(input) - totalUnsafe)