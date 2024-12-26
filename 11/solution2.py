from functools import cache

stones  = [int(x) for x in open("input.txt", "r+").read().split(" ")]

@cache
def blink(number, depth):
	if depth == 75:
		return 1
	else:
		if number == 0:
			return blink(1, depth+1)
		elif len(str(number)) % 2 == 0:
			return blink(int(str(number)[:round(len(str(number))/2)]), depth+1) \
				+ blink(int(str(number)[round(len(str(number))/2):]), depth+1)
		else:
			return blink(number * 2024, depth+1)

total = 0
for stone in stones:
	total += blink(stone, 0)

print(total)
