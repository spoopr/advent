import re

input = open("input.txt", "r+").read().splitlines()

def isSafe(levels):
	increasing = levels[0] < levels[1]
	for a,b in zip(levels, levels[1:]):
			if not ((1 <= abs(a - b) <= 3) and ((a < b) == increasing)):
				return False
	return True

totalSafe = 0
for line in input:
	levels = [int(x) for x in re.findall(r"\d+", line)]
	if isSafe(levels):
		print(f"{levels} is safe")
		totalSafe += 1 
		continue
	else:
		for i in range(len(levels)):
			levelsCopy = levels[:i] + levels[i+1:]
			if isSafe(levelsCopy):
				print(f"modification {levelsCopy} is safe")
				totalSafe += 1
				break
			
		

print(totalSafe)