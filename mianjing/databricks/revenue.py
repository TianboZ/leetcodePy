from sortedcontainers import SortedDict

class CustomerRevenue:
  def __init__(self) -> None:
    self.id = 0
    self.idToRevenue = {}
    self.revenueToIds = SortedDict({})
  
  def insert(self, revenue)->int:
    id = self.id
    self.idToRevenue[id] = revenue
    self.id += 1

    # build revenueIdMap
    if revenue in self.revenueToIds:
      self.revenueToIds.get(revenue).add(id)
    else:
      self.revenueToIds[revenue] = set([id])

    return id

  def insert2(self, revenue, referrerId):
    # old id
    oldRevenue = self.idToRevenue.get(referrerId)
    print('revenueIdMap', self.revenueToIds)
    self.revenueToIds.get(oldRevenue).remove(referrerId)
    newRevenue = oldRevenue + revenue
    if newRevenue in self.revenueToIds:
      self.revenueToIds.get(newRevenue).add(referrerId)
    else:
      self.revenueToIds[newRevenue] = set([referrerId])

    self.idToRevenue[referrerId] = newRevenue

    # new id 
    self.insert(revenue)

  def getKLowestRevenue(self, k, targetRevenue):
    print('getKLowestRevenue')
    idx = self.revenueToIds.bisect_left(targetRevenue)
    if idx < len(self.revenueToIds):
      cnt = 0
      while idx + cnt < len(self.revenueToIds) and cnt < k:
        k, v = self.revenueToIds.peekitem(idx + cnt)
        print(k, v)
        cnt += 1

customer = CustomerRevenue()
customer.insert(10)
customer.insert2(20, 0)
customer.insert2(40 , 1)

print(customer.idToRevenue, customer.revenueToIds)


customer.getKLowestRevenue(2, 35)