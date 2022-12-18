elves = [sum(elf) for elf in [[int(y.replace("'","")) for y in x.split("\\n")] for x  in repr(open("input.txt", "r+").read()).split("\\n\\n")]]

elves.sort(reverse=True)

print(sum(elves[:3]))
