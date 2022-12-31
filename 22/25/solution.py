import math, sys, time, multiprocessing, itertools

input = open("input.txt", "r").read().splitlines()


def from_snafu(_input):
    return int(_input.replace("=", "0").replace("-", "0"), 5) - int(_input.replace("2", "0").replace("1", "0").replace("=", "2").replace("-", "1"), 5)


computed = [from_snafu(line) for line in input]
_sum = sum(computed)


def branch(base):
    return list(map(lambda y, x: y + x, ("2", "1", "0", "-", "="), itertools.cycle((base,))))


if __name__ == "__main__":
    print(_sum)
    _index = 0
    _tree = {0: {"2", "1", "0", "-", "="}}
    in_decimal = {}
    with multiprocessing.Pool(processes=10) as _pool:
        try:
            while True:
                _index -= 1
                print(_index)
                start = time.time()
                _tree[_index] = set(itertools.chain.from_iterable(_pool.map(branch, _tree[_index + 1])))
                print(time.time() - start)
                start = time.time()
                if _sum in list(_pool.map(from_snafu, [x for x in _tree[_index] if not x[0] in ("=", "-")])):
                    for x in _tree[_index]:
                        if from_snafu(x) == _sum:
                            print(x)
                            raise KeyboardInterrupt
                print(time.time() - start)
        except KeyboardInterrupt:
            pass

# num = "".join(["0" for x in range(1000)])
#
# while from_snafu(num) != _sum:
#    difference = abs(_sum - from_snafu(num))
#    _2 = round(math.log(difference / 2, 5))
#    _1 = round(math.log(difference, 5))
#
#    #print(_2, _1, difference)
#
#    if (num[-1 * _1 - 1] != "0" and num[-1 * _2 - 1] != "0"):
#        leading = max([(0 if "2" not in num else num.rindex("2")), (0 if "1" not in num else num.rindex("1"))])
#        if leading == num.rindex("2"):
#            num = "".join(["0" for x in range(1000)])
#            num = num[:leading - 1] + "1" + num[leading:]
#        else:
#            num = "".join(["0" for x in range(1000)])
#            num = num[:leading] + "2" + num[leading + 1:]
#
#    if abs(difference - 2 * (5 ** _2)) < abs(difference - 5 ** _1):
#        num = num[:-1 * _2 - 1] + ("2" if (_sum - from_snafu(num)) > 0 else "=") + num[-1 * _2:]
#    else:
#        num = num[:-1 * _1 - 1] + ("1" if (_sum - from_snafu(num)) > 0 else "-") + num[-1 * _1:]
#    sys.stdout.write(f"\r{from_snafu(num)},  {_sum - from_snafu(num)}")
#    sys.stdout.flush()
#    # print(from_snafu(num))
#    # print(num)
#    if len(num) != 1000:
#        raise KeyError
#
# print(num)
