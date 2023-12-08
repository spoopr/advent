
part = False

if part:
  handKey = {line.split(" ")[0]: int(line.split(" ")[1]) for line in open("input.txt", "r+").read().splitlines()}
  valueKey = {hand: [value for value, condition in {7: lambda x: 5 in x, 6: lambda x: 4 in x, 5: lambda x: 3 in x and 2 in x, 4: lambda x: 3 in x, 3: lambda x: x.count(2) >= 2 , 2: lambda x: 2 in x, 1: lambda x: 1 in x}.items() if condition([list(hand).count(x) for x in set(hand)])][0] for hand in handKey.keys()}
  print(sum([(index+1) * handKey[card] for index, card in enumerate([x for value in range(1,8) for x in sorted([card for card in handKey.keys() if valueKey[card] == value], key=lambda card: int("".join([{"A": "c", "K": "b", "Q": "a", "J": "9", "T": "8", "9": "7", "8": "6", "7": "5", "6": "4", "5": "3", "4": "2", "3": "1", "2": "0"}[letter] for letter in list(card)]), 13))])]))
else:
  handKey = {line.split(" ")[0]: int(line.split(" ")[1]) for line in open("input.txt", "r+").read().splitlines()}
  def a(hand):
    amount = {x : list(hand).count(x) for x in set(hand)}
    jokers = amount.get("J", 0)
    amount["J"] = 0
    amount[sorted(amount, key=lambda x : amount[x], reverse=True)[0]] += jokers
    amount = list(amount.values())
    if 5 in amount:
      return 7
    elif 4 in amount:
      return 6
    elif 3 in amount and 2 in amount:
      return 5
    elif 3 in amount:
      return 4
    elif amount.count(2) >= 2:
      return 3
    elif 2 in amount:
      return 2
    else:
      return 1
  valueKey = {hand : a(hand) for hand in handKey.keys()}
  print(sum([(index+1) * handKey[card] for index, card in enumerate([x for value in range(1,8) for x in sorted([card for card in handKey.keys() if valueKey[card] == value], key=lambda card: int("".join([{"A": "c", "K": "b", "Q": "a", "T": "9", "9": "8", "8": "7", "7": "6", "6": "5", "5": "4", "4": "3", "3": "2", "2": "1", "J": "0"}[letter] for letter in list(card)]), 13))])]))