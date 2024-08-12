from bisect import bisect_right
from collections import defaultdict

class SnapshotSet:
  def __init__(self) -> None:
    # store all values, not remove from it
    self.arr = []
    
    # when iterator is called, id++
    self.id = 0

    # valueHistoryMap is dict, key is value in self.arr, 
    # value is list of tuple representing history opertions
    # tuple: (id, boolean that indicates add or delete)
    # e.g.   <2: [(id1, true), (id2, false)]>  
    self.valueHistoryMap = defaultdict(list)
    return

  def add(self, val):
    if val in self.valueHistoryMap:
      self.valueHistoryMap[val].append((self.id, True))
    else:
      self.arr.append(val)
      self.valueHistoryMap[val].append((self.id, True))

    return
  
  def remove(self, val):
    if val not in self.valueHistoryMap:
      return
    
    # already removed
    if not self.valueHistoryMap[val][-1][1]:
      return
    
    self.valueHistoryMap[val].append((self.id, False))
    
    return

  def contains(self, val)->bool:
    if val not in self.arr:
      return False
    
    return self.valueHistoryMap.get(val, [])[-1][1]
    
  def iterator(self):
    currId = self.id
    self.id += 1
    return Iterator(currId, self.arr, self.valueHistoryMap, len(self.arr))


class Iterator:
  def __init__(self, id, arr, valueHistoryMap, size):
    self.id = id
    self.arr = arr
    self.valueHistoryMap = valueHistoryMap
    self.currIdx = -1
    self.size = size

  def next(self):
    idx = self.nextIndex()
    if idx == None:
      return None
    
    res= self.arr[idx]
    self.currIdx = idx
    return res

  def hasNext(self):
    res = self.nextIndex()
    # print('hasNext', res)
    if res == None:
      return False
    # print('hasNext true')
    return True    

  def nextIndex(self):
    nextIdx = self.currIdx + 1
    while nextIdx < self.size:
      val = self.arr[nextIdx]
      historys = self.valueHistoryMap.get(val)
      # print('historys', historys)
      idx = bisect_right(historys, self.id, key= lambda x:x[0])
      
      if idx > 0 and historys[idx - 1][1]:
        return nextIdx
      nextIdx += 1
    return None

ss = SnapshotSet()
ss.add(5)
ss.add(2)
ss.add(8)
ss.remove(5)

print(ss.valueHistoryMap, ss.arr, ss.contains(2))
it = ss.iterator()   

ss.add(1)
ss.remove(2)

it2 = ss.iterator()

print('it1')
while it.hasNext():
  print(it.next())   # 2, 8

print('it2')
while it2.hasNext():
  print(it2.next()) # 1, 8