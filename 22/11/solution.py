import itertools, math, operator, copy
from pathos.multiprocessing import ProcessingPool as Pool


class monkey:
    def __init__(self, text):
        self.items = [int(x) for x in text[1].replace("Starting items:", "").replace(" ", "").split(",")]
        self.operation = eval(f"lambda old : math.floor(({text[2].split('=')[1]})%10000)")
        self.test_num = int(text[3].split(" ")[-1])
        self.test_true = f"Monkey {text[4].split(' ')[-1]}"
        self.test_false = f"Monkey {text[5].split(' ')[-1]}"
        self.inspected = 0


def test(_monkey, num):
    if (changed_num := _monkey.operation(num)) % _monkey.test_num == 0:
        # monkeys[_monkey.test_true].items.append((changed_num,))
        return (_monkey.test_true, changed_num)
    else:
        # monkeys[_monkey.test_false].items.append((changed_num,))
        return (_monkey.test_false, changed_num)


monkeys = {(text := monkeytext.splitlines())[0][:-1]: monkey(text) for monkeytext in open("input.txt", "r").read().split("\n\n")}


def run(_monkey, num):
    _monkeys = {x: 0 for x in monkeys}
    for x in range(10000):
        while True:
            b = _monkey
            _monkeys[_monkey] += 1
            _monkey, num = test(monkeys[_monkey], num)
            if int(b[-1]) >= int(_monkey[-1]):
                break
    return (_monkeys.values(), num)


if __name__ == "__main__":
    totals = [0 for x in monkeys]
    with Pool(nodes=8) as _pool:
        a = [monkey for monkey, _class in monkeys.items() for item in _class.items]
        b = [item for monkey, _class in monkeys.items() for item in _class.items]
        originals = copy.copy(b)
        print(a, b)
        items = _pool.map(run, a, b)
        b = []
        for total, num in items:
            b.append(num)
            print(total, totals)
            totals = map(operator.add, totals, total)

    totals = sorted(list(totals), reverse=True)
    print(b)

    print(totals[0] * totals[1])
    print(run("Monkey 0", 79))

# [3,0,0,2]
# for roundNum in range(10000):
#  d += 1
#  print(d)
#  for _monkey in monkeys.values():
#    b = list(map(test, itertools.cycle([_monkey]), _monkey.items))
#    _monkey.inspected += len(_monkey.items)
#    _monkey.items = []

# a = sorted([_monkey.inspected for _monkey in monkeys.values()], reverse=True)
# print(monkeys["Monkey 0"].items)
# print(f"\n{a[0] * a[1]}")
