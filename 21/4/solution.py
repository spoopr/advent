import re
import numpy as np
import copy

part = False

if part:
  file = open("input.txt", "r+").read().split("\n\n")
  nums = [int(x) for x in re.findall("\d{1,2}", file[0])]
  boards = [np.reshape(np.fromiter(re.findall("\d{1,2}", board), dtype=int), (5,5)) for board in file[1:]]
  drawn = nums[:5]
  for drawnNum in nums[5:]:
    drawn.append(drawnNum)
    for board in boards:
      check = np.isin(board, drawn)
      for x in range(5):
        if all(check[x]):
          winner = board
          break
      for y in range(5):
        if all(check[:,y]):
          winner = board
          break
      if "winner" in locals():
        break
    if "winner" in locals():
      break
  print(winner[np.invert(check)].sum() * drawnNum)
else:
  file = open("input.txt", "r+").read().split("\n\n")
  nums = [int(x) for x in re.findall("\d{1,2}", file[0])]
  boards = [np.reshape(np.fromiter(re.findall("\d{1,2}", board), dtype=int), (5,5)) for board in file[1:]]
  drawn = nums[:5]
  nextRound = []
  for drawnNum in nums[5:]:
    drawn.append(drawnNum)
    while boards:
      winner = False
      board = boards.pop(0)
      check = np.isin(board, drawn)
      for x in range(5):
        if all(check[x]):
          winner = True
          break
      for y in range(5):
        if all(check[:,y]):
          winner = True
          break
      if winner and len(boards) + len(nextRound) == 0:
        loser = board
        break
      elif not winner:
        nextRound.append(board)
    boards = copy.copy(nextRound)
    nextRound.clear()
    if "loser" in locals():
      break
  print(loser[np.invert(np.isin(loser, drawn))].sum() * drawnNum)