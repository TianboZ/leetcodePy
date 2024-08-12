from bisect import bisect_right
from collections import defaultdict

class SnapshotSet:
  def __init__(self):
    # when iterator is called, id increment by 1
    self.id = 0   

    # list store all elements, never removed from it
    self.values = []
    
    # dict <value, history operations>
    # e.g. <1, [(id1, true), (id1, false)]>      true: add  false: delete
    self.valueHistoryMap = defaultdict(list)
  
  def add(self, e):
    if e not in self.valueHistoryMap:
      self.values.append(e)
    self.valueHistoryMap[e].append((self.id, True))
  
  def remove(self, e):
    if e not in self.valueHistoryMap:
      return
    if not self.valueHistoryMap[e][-1][1]:
      return
  
    self.valueHistoryMap[e].append((self.id, False))
  
  def contains(self, e):
    return e in self.valueHistoryMap and self.valueHistoryMap[e][-1][1]
  
  def iterator(self):
    currVid = self.id
    self.id += 1
    return Iterator(self.valueHistoryMap, self.values, len(self.values), currVid)

class Iterator:
  def __init__(self, valueHistoryMap, values, value_length, vid):
    self.valueHistoryMap = valueHistoryMap
    self.values = values
    self.value_length = value_length
    self.vid = vid
    self.used_index = -1
  
  def has_next(self):
    return self.next_index() is not None
  
  def next(self):
    next_index = self.next_index()
    if next_index is None:
      return None
    self.used_index = next_index
    return self.values[next_index]

  def next_index(self):
    next_index = self.used_index + 1
    while next_index < self.value_length:
      value_history = self.valueHistoryMap[self.values[next_index]]
      print('value_history', value_history)
      iter_id = bisect_right(value_history, self.vid, key = lambda x : x[0]) - 1
      if 0 <= iter_id and value_history[iter_id][1]:
        return next_index
      next_index += 1
    return None
    
# snapshotSet = SnapshotSet()
# snapshotSet.add(1)
# snapshotSet.add(2)
# itr1 = snapshotSet.iterator()
# print(itr1.next()) # 1
# snapshotSet.add(3)
# snapshotSet.remove(2)
# print(itr1.next()) # 2
# print(itr1.next()) # None
# itr2 = snapshotSet.iterator(); # 1, 3
# print(itr2.next()) # 1
# print(itr2.next()) # 2
# print(itr2.next()) # None

ss = SnapshotSet()
ss.add(5)
ss.add(2)
ss.add(8)

ss.remove(5)
it = ss.iterator()

ss.add(1)
print(ss.contains(2)) # true

ss.remove(2)
print(ss.contains(2)) # false

print(it.valueHistoryMap)
while it.has_next():
  print(it.next()) # 2,8

