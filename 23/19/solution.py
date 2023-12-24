import os
import re

os.chdir(os.getcwd()+r"/23/19")

part = True

if part:
  file = open("input.txt", "r+").read()
  rules, scraps = file.split("\n\n")
  rulebook = {}
  for rule in rules.splitlines():
    name, conditions = rule.split("{")
    conditions = conditions[:-1]
    rulebook[name] = [condition.split(":") for condition in conditions.split(",")]
  asum = 0
  for scrap in scraps.splitlines():
    x,m,a,s = [int(i) for i in re.findall(r"\d+", scrap)]
    workflow = "in"
    while True:
      for condition in rulebook[workflow]:
        if len(condition) == 1:
          workflow = condition[0]
          break
        else:
          condition, result = condition
          if eval(condition):
            workflow = result
            break
      if workflow == "A":
        asum += sum([x,m,a,s])
        break
      elif workflow == "R":
        break
  print(asum)    
 