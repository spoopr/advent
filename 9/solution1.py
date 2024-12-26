
input = [int(x) for x in open("input.txt", "r+").read()]

disk = []
index = 0
id = 0
while index < len(input):
	disk.extend([id]*input[index])
	index += 1
	if index >= len(input):
		break
	disk.extend(["."]*input[index])
	index += 1
	id += 1

left = 0
right = len(disk) - 1
while True:
	while disk[left] != ".":
		left += 1
	while disk[right] == ".":
		right -= 1
	if right < left:
		break
	else: 
		disk[left] = disk[right]
		disk[right] = "."

total = 0
for index, value in enumerate(disk):
	if value == ".":
		break
	else:
		total += index * value

print(total)
	