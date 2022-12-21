import numpy, math, itertools, copy
check = "0abcdefghijklmnopqrstuvwxyzSE"
geomap = numpy.array([[check.index(x) for x in list(y)]for y in open("input.txt","r").read().splitlines()])
height, width = geomap.shape
#ygrid,xgrid = numpy.mgrid[0:height,0:width]
#
#print(geomap.shape)
#print(len(geomap))
#
#fullmap = numpy.dstack((xgrid,ygrid,geomap))


def get_neighbors(set):
  def neighbor(y,x,value):
    try:
      return (x,y, True if math.dist([value], [geomap[y, x].astype(int).item()]) <= 1 else False) if ( x> -1) and (y > -1) else False
    except IndexError:
      pass
  value = geomap[y,x].astype(int).item()
  return (
    (0,-1) if neighbor(y-1,x,value) else (0,0),
    (1,0) if neighbor(y,x+1,value) else(0,0),
    (0, 1) if neighbor(y+1,x,value) else (0,0),
    (-1, 0) if neighbor(y,x-1,value) else (0,0)
  )
#
#
#print(numpy.extract(numpy.apply_along_axis(lambda x: True if "S" in x else False, 2, fullmap), fullmap))

y,x = numpy.where(geomap==27)
pos = {x.tolist() + y.tolist(),}
