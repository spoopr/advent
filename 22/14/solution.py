import numpy as np
import operator, sys

np.set_printoptions(threshold=np.inf, linewidth=np.inf)
input = "[[" + open('input.txt', 'r').read().replace(' -> ', '],[').replace('\n', ']]\n[[') + "]]"
lines = [eval(x) for x in input.splitlines()]
_max = max(max(max(lines)))

_map = np.array([["." for x in range(700)] for y in range(700)])


def hard_drop(x, y):
    return (x, y+min(np.append(np.where(_map[y:,x] == "#")[0], np.where(_map[y:,x] == "O")[0]))-1)


def slide(x, y):
    #print(x,y)
    a = _map[y + 1, x - 1]
    #print(a)
    if _map[y+1, x] == ".":
        return (x, y+1)
    elif not (a == "#" or a == "O"):
        return slide(x - 1, y + 1)
    elif not (_map[y + 1, x + 1] == "#" or _map[y + 1, x + 1] == "O"):
        return slide(x + 1, y + 1)
    else:
        return (x, y)


if __name__ == "__main__":
    for line in lines:
        pos = line[0]
        _map[pos[1], pos[0]] = "#"
        for point in line:
            move = list(map(operator.sub, point, pos))
            for x in range(abs(move[0])):
                pos[0] += 1 if move[0] > 0 else -1
                _map[pos[1], pos[0]] = "#"
            for y in range(abs(move[1])):
                pos[1] += 1 if move[1] > 0 else -1
                _map[pos[1], pos[0]] = "#"
    _map[0, 500] = "+"
    _map[max(np.where(_map == '#')[0] + 2), :] = "#"
    dropped = 0
    try:
        while True:
            last_pos = (500, 0)
            pos = last_pos
            while True:
                pos = hard_drop(pos[0], pos[1])
                if pos[1] < 0:
                    raise ValueError
                #print(pos)
                pos = slide(pos[0], pos[1])
                #print(pos)
                if pos != last_pos:
                    last_pos = pos
                else:
                    break
            _map[pos[1], pos[0]] = "O"
            dropped += 1
            sys.stdout.write(f"\r{dropped}")
            sys.stdout.flush()
    except ValueError as e:
        print(_map[:max(np.where(_map == '#')[0] + 2), min(np.where(_map == '#')[1]):])
        print(e)
    print(dropped)


