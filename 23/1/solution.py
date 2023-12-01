import re

part = True

if part:
  print(sum(map(lambda x : int((regexList:= re.findall("\d", x))[0] + regexList[-1]), open("input.txt", "r+").read().splitlines())))
else:
  print(sum(map(lambda x : int((check := lambda x : {"one":"1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight":"8", "nine": "9"}[x] if x in ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine") else x)((regexList := [x[i.start(1):i.end(1)] for i in re.finditer("(?=(\d|one|two|three|four|five|six|seven|eight|nine))",x)])[0]) + check(regexList[-1])), open("input.txt", "r+").read().splitlines())))

