import re

input = open("input.txt", "r+").read().splitlines()

def branchCheck(target, value, numbers):
	if len(numbers) == 0:
		return value == target
	
	elif value > target:
		return False
	
	return branchCheck(target, value + numbers[0], numbers[1:]) or branchCheck(target, value * numbers[0], numbers[1:])
		

total = 0
for equation in input:
	target, *numbers = [int(x) for x in re.findall(r"\d+", equation)]
	if branchCheck(target, numbers[0], numbers[1:]):
		total += target

print(total)	
	