
input = [list(x) for x in open("input.txt", "r+").read().splitlines()]

x,y = -1, -1
while x == -1:
	y += 1
	for index, value in enumerate(input[y]):
		if value == "^":
			x = index
			break

visited = set()
moves = [(0,-1), (1,0), (0,1), (-1,0), (0,-1)]

move = moves[0]
while 0 <= x+move[0] < len(input[0]) and 0 <= y+move[1] < len(input):
	visited.add((x,y))
	if input[y+move[1]][x+move[0]] == "#":
		move = moves[moves.index(move)+1]
	else:
		x += move[0]
		y += move[1]
visited.add((x,y))

print(len(visited))