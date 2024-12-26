
input = [[int(y) for y in x] for x in open("input.txt", "r+").read().splitlines()]

trailheads = set()
for yIndex, row in enumerate(input):
	for xIndex, value in enumerate(row):
		if value == 0:
			trailheads.add((xIndex,yIndex))

moves = [(1,0), (0,-1), (-1,0), (0,1)]
total = 0
for x,y in trailheads:
	height = 0
	paths = [(x,y)]
	nextPaths = []
	while height < 9 and paths:
		for x,y in paths:
			for move in moves:
				nextStep = (x + move[0], y + move[1])
				if 0 <= nextStep[0] < len(input[0]) \
					and 0 <= nextStep[1] < len(input[1]) \
					and input[nextStep[1]][nextStep[0]] == height + 1:
					nextPaths.append(nextStep)

		height += 1
		paths = nextPaths
		nextPaths = []
	if height == 9:
		total += len(paths)

print(total)	