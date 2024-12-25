
input = [list(x) for x in open("input.txt", "r+").read().splitlines()]

def check(x, y, move):
	try:
		if input[y + move[1]][x + move[0]] == "M" and input[y - move[1]][x - move[0]] == "S":
			return True
	except:
		return False

moves = [
		(
			(1,1),
			(1,-1)
		), (
			(1,-1),
			(-1,-1)
		), (
			(-1,-1),
			(-1,1)
		), (
			(-1,1),
			(1,1)
		)
	]

total = 0
for y in range(len(input)-2):
	y += 1
	for x in range(len(input[0])-2):
		x += 1
		if input[y][x] == "A":
			checks = [bool(check(x,y, moveset[0]) and check(x,y, moveset[1])) for moveset in moves]
			if any(checks):
				total += 1
					
				
print(total)





			