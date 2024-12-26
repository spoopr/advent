
input = open("input.txt", "r+").read()

antennaDictionary = {x: set() for x in set(input) - {"."}}
map = [list(x) for x in input.splitlines()]

for rowIndex, row in enumerate(map):
	for columnIndex, value in enumerate(row):
		if value != ".":
			antennaDictionary[value].add((columnIndex,rowIndex))
width = len(map[0])
height = len(map)
antinodeLocations = set()
for frequency, locations in antennaDictionary.items():
	for a in locations:
		for b in locations - {a}:
			antinode = ((2 * b[0]) - a[0], (2 * b[1]) - a[1])
			if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
				antinodeLocations.add(antinode)

print(len(antinodeLocations))
	

