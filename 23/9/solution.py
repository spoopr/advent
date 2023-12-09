import os, re

part = False

os.chdir(os.getcwd()+r"\23\9")

if part:
    file = open("input.txt", "r+").read().splitlines()
    asum = 0
    for line in file:
        historys = [[int(x) for x in re.findall("[-]?\d{1,100}", line)]]
        while not all(x == 0 for x in historys[-1]):
            historys.append([historys[-1][y+1] - historys[-1][y] for y in range(len(historys[-1])-1)])
        for index in range(1, len(historys)+1):
            historys[-1 * index].append(historys[(-1*index)+1][-1]+historys[-1 * index][-1] if index > 1 else 0)
        asum += historys[0][-1]
    print(asum)

else:
    file = open("input.txt", "r+").read().splitlines()
    asum = 0
    for line in file:
        historys = [[int(x) for x in re.findall("[-]?\d+", line)][::-1]]
        while not all(x == 0 for x in historys[-1]):
            historys.append([historys[-1][y+1] - historys[-1][y] for y in range(len(historys[-1])-1)])
        for index in range(1, len(historys)+1):
            historys[-1 * index].append(historys[(-1*index)+1][-1]+historys[-1 * index][-1] if index > 1 else 0)
        asum += historys[0][-1]
    print(asum)