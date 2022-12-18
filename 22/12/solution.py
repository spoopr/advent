import numpy
check = "0abcdefghijklmnopqrstuvwxyz"
map = numpy.array([[check.index(x) if not x in "SE" else x for x in list(y)]for y in open("input.txt","r").read().splitlines()])
neighbors = lambda x,y: (map[y,x],map[y,x],map[y,x],map[y,x])