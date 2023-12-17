import os

os.chdir(os.getcwd()+r"\23\15")

part = False

if part:
  codes = open("input.txt", "r+").read().strip().split(",")
  asum = 0
  for code in codes:
    bsum = 0
    for character in code:
      bsum += ord(character)
      bsum *= 17
      bsum %= 256
    asum += bsum
  print(asum)
else:
  def hashOf(text):
    bsum = 0
    for character in text:
      bsum += ord(character)
      bsum *= 17
      bsum %= 256
    return bsum
  
  codes = open("input.txt", "r+").read().split(",")
  lensMap = {x:{} for x in range(256)}
  for code in codes:
    if code[-1] == "-":
      label = code[:-1]
      if label in lensMap[hashOf(label)]:
        lensMap[hashOf(label)].pop(label)
    else:
      label = code[:-2]
      lensMap[hashOf(label)][label] = int(code[-1])

  asum = 0
  for box, content in lensMap.items():
    if content:
      for position, lens in enumerate(content.values()):
        asum += (box+1) * (position+1) * lens
  
  print(asum)