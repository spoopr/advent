import re

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  asum = 0
  for line in file:
    line = line.split(":")[1]
    a, b = line.split("|")
    seta = {int(x) for x in re.findall("\d{1,2}", a)}
    setb = {int(x) for x in re.findall("\d{1,2}", b)}
    c = seta & setb
    asum += (2**(len(c)-1)) if c else 0
  print(asum)
else:
  file = open("input.txt", "r+").read().splitlines()
  key = {}
  for line in file:
    card, nums = line.split(":")
    seta = {int(x) for x in re.findall("\d{1,3}", nums.split("|")[0])}
    setb = {int(x) for x in re.findall("\d{1,3}", nums.split("|")[1])}
    cardNum = int(re.findall("\d{1,3}",card)[0])
    key[cardNum] = list(range(cardNum+1, cardNum+1+len(seta&setb)))
  cards = {x:1 for x in range(1, len(file)+1)}
  for card, value in cards.items():
    for copy in key[card]:
      cards[copy] += value
  print(key)
  print(cards)
  print(sum(cards.values()))
      