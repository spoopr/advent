import numpy, math, itertools, copy, operator, multiprocessing
check = "SabcdefghijklmnopqrstuvwxyzE"
geomap = numpy.array([[check.index(x) for x in list(y)]for y in open("input.txt","r").read().splitlines()])
height, width = geomap.shape
counter_map = numpy.array([[-1 for x in range(width)] for y in range(height)])

def get_neighbors(set):
  x,y = set
  def neighbor(y,x,value):
    try:
      #print(value, geomap[y,x])
      #print(math.dist([value],[geomap[y,x].astype(int).item()])<=1)
      return True if math.dist([value], [geomap[y, x].astype(int).item()]) <= 1 else False if ( x> -1) and (y > -1) else None
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

#def check(set, _queue):
 # for x in map(lambda x,y: tuple(map(operator.add, x,y)), itertools.cycle([set]),get_neighbors(set)):
  #  _queue.put(x)

if __name__ == "__main__":
  y,x = numpy.where(geomap==0)
  endy, endx = numpy.where(geomap==27)
  pos = {tuple(x.tolist() + y.tolist())}
  end = tuple(endx.tolist() + endy.tolist())
  visited = {tuple(x.tolist()+y.tolist())}
  _queue = []

  #print(get_neighbors((0,2)))
  
  cycle = 0
  with multiprocessing.Pool() as _pool:
    try:
      while True:
        print(cycle)
        _pos = copy.copy(pos)
        pos.clear()
        #_pool.starmap(check,zip(pos,itertools.cycle([_queue])))
        for _set in _pos:
          _queue.extend(map(lambda x,y: tuple(map(operator.add, x,y)), itertools.cycle([_set]),get_neighbors(_set)))
        new = set(_queue).difference(visited)
        pos = new
        
        for x in new:
          visited.add(x)
          if counter_map[x[1],x[0]] == -1:
            counter_map[x[1], x[0]] = cycle
        if end in visited:
          print(cycle+1)
          print(counter_map)
          raise KeyboardInterrupt
        cycle += 1
    except KeyboardInterrupt:
      pass
  
        
        
        

