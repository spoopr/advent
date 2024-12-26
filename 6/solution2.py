
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

def checkLoop(x, y, move):
	future = set()
	while 0 <= x+move[0] < len(input[0]) and 0 <= y+move[1] < len(input):
		if ((x,y),move) in visited or ((x,y),move) in future:
			return True		

		future.add((
			(x,y),
			move
		))
		if input[y+move[1]][x+move[0]] == "#":
			move = moves[moves.index(move)+1]
		else:	
			x += move[0]
			y += move[1]
	return False
		
startX, startY = x,y
obstructions = set()
move = moves[0]
while 0 <= x+move[0] < len(input[0]) and 0 <= y+move[1] < len(input):
	visited.add((
		(x,y),
		move
	))
	if input[y+move[1]][x+move[0]] == "#":
		move = moves[moves.index(move)+1]
	else:	
		blockedMove = moves[moves.index(move)+1]
		if checkLoop(x, y, blockedMove):
			obstructions.add((x+move[0], y+move[1]))
		x += move[0]
		y += move[1]

obstructions =  obstructions - {(startX, startY)}

for x,y in obstructions:
	input[y][x] = "O"

for y in input:
	print("".join(y))

print(len(obstructions))