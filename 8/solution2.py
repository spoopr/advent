
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
		if len(locations) > 1:
			antinodeLocations.add(a)
		for b in locations - {a}:
			antinode = [(2*b[0]) - a[0], (2*b[1]) - a[1]]
			while 0 <= antinode[0] < width and 0 <= antinode[1] < height:
				antinodeLocations.add(tuple(antinode))
				antinode[0] += b[0] - a[0]
				antinode[1] += b[1] - a[1]

print(len(antinodeLocations))
	

