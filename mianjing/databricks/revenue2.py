
"""

11:23 - 11:56

solution:

map: key is id, value is revenue
e.g.
{
  0: 40,
  1: 20,
  2: 40
}

map2: key is revenue, value is set of ids. 
{
  40: (0, 2),
  20: (1)
}
use treemap (key are sorted), easier to get_lowest_k_by_total_revenue


complexity:
- insert
time O(logn), n is map number of keys in map2

- get_lowest_k_by_total_revenue
time O(logn + k)

class: space O(n)


"""
from sortedcontainers import SortedDict


class Revenue:
  def __init__(self) -> None:
    self.id = 0
    self.idToRevenue = {}
    self.revenueToId = SortedDict({})
    
  def insert(self, revenue)->int:
    id = self.id
    self.idToRevenue[id] = revenue
    self.id += 1

    # add revenue treemap
    if revenue in self.revenueToId:
      self.revenueToId[revenue].add(id)
    else:
      ids = set()
      ids.add(id)
      self.revenueToId[revenue] = ids

    return id

  def insert2(self, revenue, referId)->int:
    # assmue referId is valid

    # process referid revenue
    oldRevenue = self.idToRevenue.get(referId)
    newTotalRevenue = oldRevenue + revenue
    self.revenueToId.get(oldRevenue).remove(referId)

    if newTotalRevenue in self.revenueToId:
      self.revenueToId.get(newTotalRevenue).add(referId)
    else:
      self.revenueToId[newTotalRevenue] = set([referId])

    # process new id
    self.insert(revenue)


  def get_lowest_k_by_total_revenue(self, k, val):
    res = set()
    
    idx = self.revenueToId.bisect_left(val)
    if idx != len(self.revenueToId):
      k, v = self.revenueToId.peekitem(idx)
      # print(k, v)

      i = 0
      while idx + i < len(self.revenueToId):
        k, v = self.revenueToId.peekitem(idx + i)
        print(k, v)
        for id in v:
          res.add(id)
        i += 1

    print('ids', res)

revenue = Revenue()
revenue.insert(10)
revenue.insert2(20, 0)
revenue.insert2(40 ,1)
revenue.insert(40)
revenue.insert(40)


print(revenue.revenueToId)

print(revenue.get_lowest_k_by_total_revenue(2, 30))
