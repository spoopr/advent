import re, math

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  print(sum([int(line[match.start(0): match.end(0)]) for index, line in enumerate(file) for match in re.finditer("\d{1,4}", line) if any(map(lambda x : re.search("[^.\d]", x[max(match.start(0) - 1, 0):min(match.end(0) + 1, len(file[0]))]) ,[file[index-1] if index >= 0 else "." * len(file[0]), line, file[index+1] if index+1 < len(file) else "." * len(file[0])]))]))
else:
  file = open("input.txt", "r+").read().splitlines()
  print(sum([math.prod([int(re.findall("\d{1,3}",_line[max(match.start(0) - 1, 0)+_match.end(0)-3:max(match.start(0) - 1, 0)+_match.end(0)])[0]) if _match.start(0) == 0 else int(re.findall("\d{1,3}",_line[max(match.start(0) - 1, 0)+_match.start(0):max(match.start(0) - 1, 0)+_match.start(0)+3])[0]) for regexIter, _line in [(re.finditer("\d{1,3}",x[max(match.start(0) - 1, 0):min(match.end(0) + 1, len(file[0]))]), x) for x in [ file[index-1] if index > 0 else "." * len(file[0]),line,file[index+1] if index < len(file) - 1 else "." * len(file[0])]] for _match in regexIter]) for index, line in enumerate(file) for match in re.finditer("\*", line) if len(list(re.finditer("\d{1,3}", "\n".join([x[max(match.start(0) - 1, 0):min(match.end(0) + 1, len(file[0]))] for x in [ file[index-1] if index > 0 else "." * len(file[0]), line, file[index+1] if index < len(file) - 1 else "." * len(file[0])]])))) == 2]))