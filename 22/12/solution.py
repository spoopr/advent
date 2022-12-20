import numpy, math
check = "0abcdefghijklmnopqrstuvwxyz"
geomap = numpy.array([[check.index(x) if not x in "SE" else x for x in list(y)]for y in open("input.txt","r").read().splitlines()])
height, width = geomap.shape
ygrid,xgrid = numpy.mgrid[0:height,0:width]

print(geomap.shape)
print(len(geomap))

fullmap = numpy.dstack((xgrid,ygrid,geomap))


neighbor = lambda y,x,value : (x,y, True if math.dist([value],[geomap[y,x]]) <= 1 else False) if ( x> -1) and (y > -1) else None
def get_neighbors(set):
  x,y, value = map(lambda x : x.astype(int).item(),set)
  neighbors = [
    neighbor(y-1,x,value),
    neighbor(y,x+1,value),
    neighbor(y+1,x,value),
    neighbor(y,x-1,value)
  ]
  
  return (x,y,value)

neighbor_map = numpy.apply_along_axis(get_neighbors,2,fullmap)

print(neighbor_map)

