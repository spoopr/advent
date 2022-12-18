#import itertools

#p1 = itertools.islice(itertools.cycle(range(1,11)),2, None)
#p2 = itertools.islice(itertools.cycle(range(1,11)),0,None)

#die = itertools.islice(itertools.cycle(range(1,101)), 100, None)

#p1_total = 0
#p2_total = 0

#a = lambda x: (9*x-3)
z = lambda a : answer if (answer:= a%10) != 0 else 10

#turn = True
#rolls = 0
#while True:
#  x = 0
#  for i in range(3):
#    x += next(die)
#    rolls += 1
#  if turn:
##    turn = False
#    for y in range(x):
#      l = next(p1)
#    p1_total += l
#  else: 
#    turn = True
#    for y in range(x):
#      l = next(p2)
#    p2_total += l
#  if p1_total >= 1000:
    #print(p1_total,p2_total,rolls,p2_total*rolls)
#    break
#  if p2_total >= 1000:
    #print(p1_total,p2_total,rolls,p1_total*rolls)
#    break

p1 = 4
p2 = 8
turn = True


p1_total = 0
p2_total = 0

def calculate(pos, strategy=False):
  rolls = 0
  total = 0
  while True:
    options = [z(pos+x) for x in range(3,10)]
    options.sort(reverse=strategy)
    rolls += 3
    total += options[0]
    if total >= 21:
      return rolls, total

print((3**calculate(p1,False)[0])-(3**calculate(p1,True)[0]))