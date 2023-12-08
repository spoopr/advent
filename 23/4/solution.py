import re

part = True

if part:
  file = open("input.txt", "r+").read().splitlines()
  print(sum([(2**(len(c)-1)) if (c := {int(x) for x in re.findall("\d{1,2}",  line.split(":")[1].split("|")[0])} & {int(x) for x in re.findall("\d{1,2}",  line.split(":")[1].split("|")[1])}) else 0 for line in file]))
else:
  file = open("input.txt", "r+").read().splitlines()
  key = {(cardNum := int(re.findall("\d{1,3}",line.split(":")[0])[0])): list(range(cardNum+1, cardNum+1+len({int(x) for x in re.findall("\d{1,3}", line.split(":")[1].split("|")[0])}&{int(x) for x in re.findall("\d{1,3}", line.split(":")[1].split("|")[1])}))) for line in file}
  cards = {x:1 for x in range(1, len(file)+1)}
  for card, value in cards.items():
    for copy in key[card]:
      cards[copy] += value
  print(sum(cards.values()))
      