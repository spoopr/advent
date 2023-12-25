import os

os.chdir(os.getcwd() + r"\23\20")

part = False

if part:
  file = open("input.txt", "r+").read().splitlines()
  nodeKey = {line[1:3] if (isBroadcaster := line.split()[0] != "broadcaster") else line.split()[0]: (line[0] if isBroadcaster else 0, line.replace(" ", "").split("->")[1].split(",")) for line in file}
  parentKey = {line[1:3]: [parent for parent in nodeKey if line[1:3] in nodeKey[parent][1]] for line in file}
  
  print(nodeKey)
  
  state = {node: False for node in nodeKey} 
  pulses = {True: 0, False: 0}
  for i in range(1000):
    unprocessed = [("broadcaster", False)]
    pulses[False] += 1
    while unprocessed:
      node, input = unprocessed.pop(0)
      if not node in nodeKey:
        continue
      if nodeKey[node][0] == "&":
        state[node] = not all(state[parent] for parent in parentKey[node])
        unprocessed.extend((child, state[node]) for child in nodeKey[node][1])
        pulses[state[node]] += len(nodeKey[node][1])
      elif nodeKey[node][0] == "%":
        if not input:
          state[node] = not state[node]
          unprocessed.extend((child, state[node]) for child in nodeKey[node][1])
          pulses[state[node]] += len(nodeKey[node][1])
      elif node == "broadcaster":
        unprocessed.extend((child, False) for child in nodeKey[node][1])    
        pulses[False] += len(nodeKey["broadcaster"][1])

  print(pulses[True], pulses[False])
  print(pulses[True] * pulses[False])

else:
  file = open("input.txt", "r+").read().splitlines()
  nodeKey = {line[1:3] if (isBroadcaster := line.split()[0] != "broadcaster") else line.split()[0]: (line[0] if isBroadcaster else 0, line.replace(" ", "").split("->")[1].split(",")) for line in file}
  parentKey = {line[1:3]: [parent for parent in nodeKey if line[1:3] in nodeKey[parent][1]] for line in file}
  
  state = {node: False for node in nodeKey} 
  pulses = {True: 0, False: 0}
  i = 0
  while True:
    i += 1
    print(i)
    unprocessed = [("broadcaster", False)]
    pulses[False] += 1
    while unprocessed:
      node, input = unprocessed.pop(0)
      if node == "rx" and not input:
        print(i+1)
      if not node in nodeKey:
        continue
      if nodeKey[node][0] == "&":
        state[node] = not all(state[parent] for parent in parentKey[node])
        unprocessed.extend((child, state[node]) for child in nodeKey[node][1])
        pulses[state[node]] += len(nodeKey[node][1])
      elif nodeKey[node][0] == "%":
        if not input:
          state[node] = not state[node]
          unprocessed.extend((child, state[node]) for child in nodeKey[node][1])
          pulses[state[node]] += len(nodeKey[node][1])
      elif node == "broadcaster":
        unprocessed.extend((child, False) for child in nodeKey[node][1])    
        pulses[False] += len(nodeKey["broadcaster"][1])