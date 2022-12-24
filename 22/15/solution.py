import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

input = "((" + open("input.txt", "r").read().replace(" y=", "").replace("Sensor at x=", "").replace(": closest beacon is at x=", "),(").replace("\n", "))\n((") + "))"

pairs = [eval(x) for x in input.splitlines()]

flattened = [z for x in pairs for y in x for z in y]

print(pairs)
_max = max(flattened)
_min = min(flattened)
print(_max, _min)

_map = np.array(["." for x in range(_max + 2000000000 - _min)])

a = lambda i, k: sum(map(lambda x, y: abs(x - y), i, k))

for sensor, beacon in pairs:
    coverage = a(sensor, beacon)
    if (dist := abs(sensor[1] - 2000000)) <= coverage:
        x = sensor[0] - (coverage - dist) + 100000000 - _min
        y = sensor[0] + 1 + (coverage - dist) + 1000000000 - _min
        print(sensor, coverage)
        print(x, y)
        _map[x:y] = "#"

# print(_map[999990:-999990])
print(np.where(_map == "#")[0].shape[0])
# 905832529 is way to fukcing high
