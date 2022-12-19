import itertools, math
from pathos.multiprocessing import ProcessingPool as Pool

class monkey:
  def __init__(self,text):
    self.items = [(int(x),) for x in text[1].replace("Starting items:", "").replace(" ","").split(",")]
    self.operation = eval(f"lambda old : math.floor(({text[2].split('=')[1]}))")
    self.test_num = int(text[3].split(" ")[-1])
    self.test_true = f"Monkey {text[4].split(' ')[-1]}"
    self.test_false = f"Monkey {text[5].split(' ')[-1]}"
    self.inspected = 0

def test(_monkey, num):
  num = num[0]
  if (changed_num := _monkey.operation(num)) % _monkey.test_num == 0:
    monkeys[_monkey.test_true].items.append((changed_num,))
    return True
  else:
    monkeys[_monkey.test_false].items.append((changed_num,))
    return False

monkeys = {(text := monkeytext.splitlines())[0][:-1]: monkey(text) for monkeytext in open("input.txt", "r").read().split("\n\n")}
d = 0

for roundNum in range(10000):
  d += 1
  print(d)
  for _monkey in monkeys.values():
    b = list(map(test, itertools.cycle([_monkey]), _monkey.items))
    _monkey.inspected += len(_monkey.items)
    _monkey.items = []

a = sorted([_monkey.inspected for _monkey in monkeys.values()], reverse=True)
print(monkeys["Monkey 0"].items)
print(f"\n{a[0]*a[1]}")
