import numpy, itertools, copy, operator, multiprocessing, sys

numpy.set_printoptions(threshold=numpy.inf, linewidth=numpy.inf)

check = "SabcdefghijklmnopqrstuvwxyzE"
geomap = numpy.array([[check.index(x) for x in list(y)] for y in open("input.txt", "r").read().splitlines()])
height, width = geomap.shape
counter_map = numpy.array([[-1 for x in range(width)] for y in range(height)])


def get_neighbors(_set):
    x, y = _set

    def neighbor(y, x, _value):
        try:
            return True if _value - 1 <= geomap[y, x].astype(int).item() and (x > -1) and (y > -1) else False
        except IndexError:
            pass

    value = geomap[y, x].astype(int).item()
    return (
        (0, -1) if neighbor(y - 1, x, value) else (0, 0),
        (1, 0) if neighbor(y, x + 1, value) else (0, 0),
        (0, 1) if neighbor(y + 1, x, value) else (0, 0),
        (-1, 0) if neighbor(y, x - 1, value) else (0, 0)
    )


#
#
# print(numpy.extract(numpy.apply_along_axis(lambda x: True if "S" in x else False, 2, fullmap), fullmap))

def check(_set):
    return list(map(lambda x, y: tuple(map(operator.add, x, y)), itertools.cycle([_set]), get_neighbors(_set)))


if __name__ == "__main__":
    y, x = numpy.where(geomap == 27)
    endy, endx = numpy.where(geomap == 27)
    pos = {tuple(x.tolist() + y.tolist())}
    end = tuple(endx.tolist() + endy.tolist())
    visited = {tuple(x.tolist() + y.tolist())}

    print(geomap)

    cycle = 0
    with multiprocessing.Pool(8) as _pool:
        try:
            while True:
                sys.stdout.write(f"\r{cycle}")
                sys.stdout.flush()
                _queue = []
                _pos = copy.copy(pos)
                pos.clear()
                X = _pool.map(check, _pos)
                # for _set in _pos:
                #    _queue.extend(
                #        map(lambda x, y: tuple(map(operator.add, x, y)), itertools.cycle([_set]), get_neighbors(_set)))
                for x in X:
                    _queue.extend(x)
                new = set(_queue).difference(visited)
                pos = new
                for x in new:
                    visited.add(x)
                    if counter_map[x[1], x[0]] == -1:
                        counter_map[x[1], x[0]] = cycle
                # if end in visited:
                #    raise KeyboardInterrupt
                for x, y in new:
                    if geomap[y, x] == 1:
                        raise KeyboardInterrupt
                cycle += 1
        except KeyboardInterrupt:
            pass
        print("\n", counter_map, "\n")
        print(cycle + 1)
