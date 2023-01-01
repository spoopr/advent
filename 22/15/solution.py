import numpy as np
import copy

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

input = "((" + open("input.txt", "r").read().replace(" y=", "").replace("Sensor at x=", "").replace(": closest beacon is at x=", "),(").replace("\n", "))\n((") + "))"

flattened = [z for x in [eval(x) for x in input.splitlines()] for y in x for z in y]


def check_line(line):
    # print(line)
    overlapping = []

    for sensorx, sensory, beaconx, beacony in list(zip(flattened, flattened[1:], flattened[2:], flattened[3:]))[::4]:
        if (size := (abs(sensorx - beaconx) + abs(sensory - beacony)) - abs(sensory - line)) > -1:
            # print(size, sensorx, sensory, beaconx, beacony)
            overlapping.append((sensorx - size, sensorx + size))

    def check_overlaps(_list):
        new_list = copy.copy(_list)
        try:
            for start, end in _list:
                pair = [start, end]
                for x, y in _list:
                    if not (x == start and y == end):
                        if x < start and y >= start:
                            pair[0] = x
                        if y > end and x <= end:
                            pair[1] = y
                        if pair[0] == x or pair[1] == y:
                            # print(new_list)
                            # print(start,end,x,y)
                            # print(pair)
                            new_list.remove((start, end))
                            new_list.remove((x, y))
                            new_list.append(tuple(pair))
                            raise KeyboardInterrupt
        except KeyboardInterrupt:
            return check_overlaps(new_list)
        return new_list

    filled = check_overlaps(overlapping)

    # print(overlapping)
    # print(filled)

    total = sum([abs(x - y) + 1 for x, y in filled])

    beacons = []
    for sensorx, sensory, beaconx, beacony in list(zip(flattened, flattened[1:], flattened[2:], flattened[3:]))[::4]:
        if beacony == line:
            for start, end in filled:
                if start <= beaconx and end >= beaconx:
                    if not beaconx in beacons:
                        beacons.append(beaconx)
                        total -= 1
                        break

    # print(total)
    # print(filled)
    # print(overlapping)

    if len(filled) > 1:
        print(filled)
        return filled

for x in range(0, 4000001):
    print(x)
    filled = check_line(x)
    if filled != None:
        break
if filled[0][1] == filled[1][0] - 2:
    print(filled[1][0] - 1, x)
    print((filled[1][0] - 1) * 4000000 + x)
elif filled[1][1] + 2 == filled[0][0]:
    print(filled[1][1] + 1, x)
    print((filled[1][1] + 1) * 4000000 + x)
# print(beacons)

# 905832529 is way to fukcing high
# 4568012 too low
