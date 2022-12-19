import sys, itertools, copy

packets = [eval(x) for x in open("input.txt", "r").read().replace("'", "").replace("\n\n", "\n").split("\n")]
packet_len = len(packets)
packets.extend([[[2]], [[6]]])

a = lambda x: [x] if not isinstance(x, list) else x


def check(list1, list2, b=False):
    if b:
        pass
        print(list1, list2)
    try:
        for x in range(len(list1)):
            value1 = list1[x]
            value2 = list2[x]
            if isinstance(value1, list) or isinstance(value2, list):
                if a(value1) != a(value2):
                    return check(a(value1), a(value2), b=False)
            elif value1 < value2:
                return True
            elif value1 > value2:
                return False
        return True
    except IndexError:
        return False


#chain = [[x for x in packets if list(map(check, packets, itertools.cycle([x]))).count(True) == 1][0]]
#packets.remove(chain[0])
#
#print(packets)
#def path(_chain, options, recursion):
#  recursion += 1
#  print(recursion)
#  for x in options:
#      if check(_chain[-1], x):
#          a = copy.copy(options)
#          a.remove(x)
#          b = copy.copy(_chain)
#          b.append(x)
#          if a == []:
#            return b
#          if (returned := path(b,a,recursion)) != False:
#            return returned
#  return False
#
#print(path(chain,packets,0))

exclusive_chains = []
exclusive_chains.append([x for x in packets if list(map(check,packets,itertools.cycle([x]))).count(True) ==1])
exclusive_chains.append([x for x in packets if list(map(check,itertools.cycle([x]),packets)).count(True) ==1])
packets.remove(exclusive_chains[0][0])
packets.remove(exclusive_chains[1][0])
d=0
while d < 500:
 d += 1
 print(len(exclusive_chains))
 for x in packets:
   if list(map(check,packets,itertools.cycle([x]))).count(True) ==1:
     for chain in exclusive_chains:
       if check(chain[-1],x):
         chain.append(x)
         packets.remove(x)
         break
     break
   elif list(map(check,itertools.cycle([x]),packets)).count(True) == 1:
     for chain in exclusive_chains:
       if check(x,chain[0]):
         chain.insert(0,x)
         packets.remove(x)
         break
     break
 for x in packets:
   matches = [y for y in packets if check(y,x) and x != y]
   if len(matches) == 1:
     exclusive_chains.append([matches[0],x])
     packets.remove(x)
     packets.remove(matches[0])
     break
   matches = [y for y in packets if check(x,y) and x != y]
   if len(matches) == 1:
     exclusive_chains.append([x,matches[0]])
     packets.remove(x)
     packets.remove(matches[0])
     break
last = exclusive_chains[1]
def path(explored,options, recursion_level):
 recursion_level += 1
 print(recursion_level)
 for x in options:
   if check(explored[-1],x[0]):
     if x[-1] == last and len(options) == 1:
       return explored + x
     a = copy.copy(options)
     a.remove(x)
     if (returned := path(explored+x,a, recursion_level)) != False:
       return returned
 return False
all = exclusive_chains + [[x] for x in packets]
all.remove(exclusive_chains[0])
ordered_packets = path(exclusive_chains[0], all,0)
print(ordered_packets)

print((ordered_packets.index([[2]])+1)*(ordered_packets.index([[6]])+1))
