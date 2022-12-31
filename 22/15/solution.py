import numpy as np
import copy

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

input = "((" + open("input.txt", "r").read().replace(" y=", "").replace("Sensor at x=", "").replace(": closest beacon is at x=", "),(").replace("\n", "))\n((") + "))"

flattened = [z for x in [eval(x) for x in input.splitlines()] for y in x for z in y]

overlapping = []

for sensorx, sensory, beaconx, beacony in list(zip(flattened, flattened[1:], flattened[2:], flattened[3:]))[::4]:
    if (size := (abs(sensorx - beaconx) + abs(sensory - beacony)) - abs(sensory - 2000000)) > -1:
        overlapping.append((sensorx - size, sensorx + size))
        print(size)


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
                        print(new_list)
                        print(start,end,x,y)
                        print(pair)
                        new_list.remove((start, end))
                        new_list.remove((x, y))
                        new_list.append(tuple(pair))
                        raise KeyboardInterrupt
    except KeyboardInterrupt:
        return check_overlaps(new_list)
    return new_list


filled = check_overlaps(overlapping)

print(overlapping)
print(filled)

total = sum([abs(x - y) + 1 for x, y in filled])

beacons = []
for sensorx, sensory, beaconx, beacony in list(zip(flattened, flattened[1:], flattened[2:], flattened[3:]))[::4]:
    if beacony == 2000000:
        for start, end in filled:
            if start <= beaconx and end >= beaconx:
                if not beaconx in beacons:
                    beacons.append(beaconx)
                    total -= 1
                    break

print(total)
print(beacons)

# 905832529 is way to fukcing high
# 4568012 too low
