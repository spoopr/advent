
input = [list(x) for x in open("input.txt", "r+").read().splitlines()]


def check(x, y, move, letter):
	try:
		x += move[0]
		y += move[1]
		if input[y][x] == letter and x >= 0 and y >= 0:
			if letter == "S":
				return True
			return check(x, y, move, "MAS"["MAS".index(letter)+1])
		else:
			return False
	except:
		return False
moves = [
		(0,1),
		(1,0),
		(1,1),
		(1,-1),
		(-1,-1),
		(-1,1),
		(-1,0),
		(0,-1)
	]
total = 0
for y in range(len(input)):
	for x in range(len(input[0])):
		if input[y][x] == "X":
			total += sum(check(x,y,move,"M") for move in moves)

print(total)





			