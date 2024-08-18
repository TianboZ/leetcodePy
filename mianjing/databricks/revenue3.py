"""
12:12 am - 12:39

solution:
- map: key is id, value is revenue
e.g. 
{
  1: 40
}

- map2: key is revenue, value is set of id
e.g. 
{
  20: (5,6)
  40: (1,2,3,4)
}
map2 is a sortedmap (treemap), log(n) to insert, log(n) to lookup k items

complexity:
1. insert()
time O(1)

2. insert2()
time O(log n)

3. get_lowest_k_by_total_revenue()
time O(logn + k)


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

    # add to revenue to id map
    if revenue in self.revenueToId:
        self.revenueToId.get(revenue).add(id)
    else:
        ids = set()
        ids.add(id)
        self.revenueToId[revenue] = ids

    return id


  def insert2(self, revenue, referId)->int:
    oldRevenue = self.idToRevenue.get(referId)
    newRevenue = oldRevenue + revenue
    self.revenueToId.get(oldRevenue).remove(referId)
    if newRevenue in self.revenueToId:
        self.revenueToId.get(newRevenue).add(referId)
    else:
        self.revenueToId[newRevenue] = set([referId])
    self.idToRevenue[referId] = newRevenue

    # process new id
    self.insert(revenue)


  def get_lowest_k_by_total_revenue(self, k, val):
    ids = []
    idx = self.revenueToId.bisect_left(val)
    if idx < len(self.revenueToId):
        # _k, _v = self.revenueToId.peekitem(idx)
        i = 0
        while idx + i < len(self.revenueToId) and i < k:
            _k, _v = self.revenueToId.peekitem(idx + i)
            print(_k, _v)
            for id in _v:
                ids.append(id)
            i += 1
    else:
        print('no such value')

    print(ids)

revenue = Revenue()
revenue.insert(10)
revenue.insert2(20, 0)
revenue.insert2(40 ,1)
# revenue.insert(40)
# revenue.insert(40)


print(revenue.revenueToId)
# print(revenue.idToRevenue)

print(revenue.get_lowest_k_by_total_revenue(2, 30))
