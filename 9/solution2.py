
input = [int(x) for x in open("input.txt", "r+").read()]

disk = []
left = 0
used = set()
while left < len(input):
	leftId = round(left/2)
	if not leftId in used:
		disk.extend([leftId] * input[left])
		used.add(leftId)
	else:
		disk.extend(["."] * input[left])
	left += 1

	if left >= len(input):
		break

	right = len(input)-1 if bool(len(input) % 2) else len(input) - 2
	free = input[left]
	while True:
		rightId = round(right/2)
		if input[right] <= free and not rightId in used:
			disk.extend([rightId]*input[right])
			used.add(rightId)
			free -= input[right]
		right -= 2
		if right < 0 or free == 0:
			break
	disk.extend(["."]*free)
	left += 1
	
total = 0
for index, value in enumerate(disk):
	if value != ".":
		total += index * value

print(total)
	