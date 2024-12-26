
stones  = [int(x) for x in open("input.txt", "r+").read().split(" ")]

for i in range(25):
	newStones = []
	for stone in stones:
		if stone == 0:
			newStones.append(1)
		elif len(str(stone)) % 2 == 0:
			newStones.append(int(str(stone)[:round(len(str(stone))/2)]))
			newStones.append(int(str(stone)[round(len(str(stone))/2):]))
		else:
			newStones.append(stone * 2024)
	stones = newStones
	newStones = []

print(len(stones))