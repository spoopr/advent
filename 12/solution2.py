
input = open("input.txt", "r+").read()

typeLocations = {x : set() for x in set(input)}
for yIndex, row in enumerate(input.splitlines()):
	for xIndex, type in enumerate(row):
		typeLocations[type].add((xIndex,yIndex))

moves = [(1,0), (0,1), (-1,0), (0,-1)]
def flood(x, y, validLocations):
	visited = {(x,y)}
	next = {(x,y)}
	while next:
		x,y = next.pop()
		visited.add((x,y))
		for move in moves:
			nextMove = (x + move[0], y + move[1])
			if nextMove in validLocations and not nextMove in visited:
				next.add(nextMove)
	return visited

def trace(region):
	perimeter = set()
	for x,y in region:
		for move in moves:
			if not (x + move[0], y + move[1]) in region:
				perimeter.add(((x,y),move))
	edges = 0
	while perimeter:
		edges += 1
		visited = {perimeter.pop()}
		next = visited.copy()
		while next:
			position, direction = next.pop()
			visited.add((position, direction))
			for move in moves:
				nextMove = ((position[0] + move[0], position[1] + move[1]), direction)
				if nextMove in perimeter and not nextMove in visited:
					next.add(nextMove)
		perimeter = perimeter - visited
	
	return edges	

total = 0
for type, locations in typeLocations.items():
	while locations:
		x,y = locations.pop()
		region = flood(x,y, locations)
		locations = locations - region
		total += len(region) * trace(region)	

print(total)
	
	


