import re, math

rules, manuals = open("input.txt", "r+").read().split("\n\n")

rulesDict = {x[:2]: set() for x in rules.splitlines()}
for rule in rules.splitlines():
	rulesDict[rule[:2]].add(rule[3:])

def check(numbers):
	for index, x in enumerate(numbers):
		if not ((index == len(numbers) - 1) or not (set(numbers[index+1:]) - rulesDict[x])):
			return False
	return True

total = 0
for manual in manuals.splitlines():
	numbers = re.findall(r"\d+", manual)
	if check(numbers):
		total += int(numbers[math.floor(len(numbers)/2)])

print(total)
