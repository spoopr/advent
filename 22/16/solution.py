import copy, itertools

input = "(" + open("input.txt", "r").read().replace(",", "', '").replace("Valve ", "'").replace(" has flow rate=", "', ").replace("; tunnels lead to valves ", ", '").replace("; tunnel leads to valve ", ", '").replace("\n", "')\n(").replace(" ", "") + "')"

lines = [eval(x) for x in input.splitlines()]

paths = {x: y for x, _, *y in lines}
rates = {x: y for x, y, *_ in lines}
status = {x: False for x, *_ in lines}
max_valves = sum([1 for x, y, *_ in lines if y > 0])

working_valves = [x for x,y,*_ in lines if y > 0]

#pressure_rate = 0
#released = 0
#pos = 'AA'
#path = []
#open_valves = 0

# def find_best(pos):
#    a = []
#    for x in pos:
#        a.extend(paths[x])
#    a = list(set(a))
#    #print(sorted(a))
#    for x in a:
#        #print(x, status[x])
#        if status[x]:
#            rates[x] = 0
#    a = sorted(a, reverse=True, key=lambda x: rates[x])
#    if rates[a[0]] == 0:
#        b = find_best(a)
#        for x in pos:
#            if b[0] in paths[x]:
#                b.insert(0, x)
#                return b
#    else:
#        for x in pos:
#            if a[0] in paths[x]:
#                return [x, a[0]]
#
#
# for _ in range(30):
#    print(pos, f"{open_valves}/{max_valves}")
#    if open_valves < max_valves:
#        if (not status[pos]) and rates[pos] != 0:
#            print(f"releasing {pos}, rate at {pressure_rate} + {rates[pos]}")
#            status[pos] = True
#            pressure_rate += rates[pos]
#            open_valves += 1
#        else:
#            if path == []:
#                path = find_best([pos])
#                path.pop(0)
#                print(f"new instructions: {path}")
#            pos = path[0]
#            print(f"moving to {pos}")
#            path.pop(0)
#    released += pressure_rate
#
# print("ran out of time")
# print(released)#

print(paths)
print(rates)
print(status)

def map(pos):
    for adjacent in paths[pos]:
        pass