import re

part = False

if part:
  file = open("input.txt", "r+").read().split(":")[1:]
  nums = [[int(y) for y in re.findall("\d{1,10}", x)] for x in file]
  seeds = nums[0]
  maps = [list(zip(mapList,mapList[1:],mapList[2:]))[::3] for mapList in nums[1:]]
  translated = []
  for seed in seeds:
    print("new seed")
    for _map in maps:
      for order in _map:
        if order[1] <= seed <= order[1] + order[2]-1:
          print(seed)
          seed += order[0] - order[1]
          break
    translated.append(seed)
  print(sorted(translated))

else:
  file = open("input.txt", "r+").read().split(":")[1:]
  nums = [[int(y) for y in re.findall("\d{1,10}", x)] for x in file]
  seedRanges = [[number, number+repetitions-1] for number,repetitions in list(zip(nums[0],nums[0][1:]))[::2]]
  maps = [list(zip(mapList,mapList[1:],mapList[2:]))[::3] for mapList in nums[1:]]
  print(maps)
  translated = []
  for seedRange in seedRanges:
    print("new seed")
    unprocessed = []
    processed = []
    unprocessed.append(seedRange)
    for _map in maps:
      print(f"map {maps.index(_map)}")
      while unprocessed:
        print(unprocessed)
        start, end = unprocessed.pop(0)
        print(start, end)
        a = len(processed)
        for orderResult, orderSource, orderLength in _map:
          print(orderResult, orderSource, orderLength)
          if orderSource <= start <= orderSource + orderLength - 1 or orderSource <= end <= orderSource + orderLength - 1:
            print(orderResult, orderSource, orderLength)
            if orderSource <= start <= orderSource + orderLength - 1:
              newStart = start + orderResult - orderSource
            else: 
              newStart = orderResult
            if orderSource <= end <= orderSource + orderLength - 1:
              newEnd = end + orderResult - orderSource
            else:
              newEnd = orderResult + orderLength 
            print(newStart, newEnd)
            if end - start == newEnd - newStart:
              processed.append([newStart,newEnd])
            elif newStart == orderResult and orderSource <= end <= orderSource + orderLength - 1: 
              processed.append([newStart, newEnd])
              unprocessed.append([start, orderSource-1])
            elif newEnd == orderResult + orderLength  and orderSource <= start <= orderSource + orderLength - 1:
              processed.append([newStart, newEnd])
              unprocessed.append([orderSource+orderLength, end])
            else:
              processed.append([newStart,newEnd])
              unprocessed.append([start, orderSource-1])
              unprocessed.append([orderSource+orderLength, end])
            break
        if len(processed) == a:
          processed.append([start,end])
        
      print("end")
      print(unprocessed, processed)
      unprocessed.extend(processed)
      processed.clear()
    translated.extend(unprocessed)
    translated = [min(translated),]
  print(translated)
  print(len([y for start,end in translated for y in range(start, end)]))
  print(min([x for x, y in translated]))