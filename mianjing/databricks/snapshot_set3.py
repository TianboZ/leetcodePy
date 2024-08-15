'''
9:36

arr: record all numbers, never remove item from it
e.g.[5, 2, 8] 

map: key is number, value is array of tuple, tuple is [id, add or move]. true is add, false is remove

e.g. {
  5: [[id1, True], [id1, False] ....   ]
  2: [[id1, True] ...  ]
  3: [[id1, True] ...  ]
}

when iterator() is called, id++, id = 1 initail 

'''

from collections import defaultdict
from bisect import bisect_left, bisect_right 

class SnapshotSet:
  def __init__(self):
    self.arr = []
    self.map = defaultdict(list)
    self.id = 1

  def add(self, val):
    if val in self.map:
      self.map[val].append([self.id, True])
    else:
      self.arr.append(val)
      self.map[val].append([self.id, True])


    # print(self.map)

  # return true if remove success
  def remove(self, val)->bool:
    if val not in self.map:
      return False
    if val in self.map and self.map[val][-1][1] == False:
      # already removed before
      return False
    
    self.map[val].append([self.id, False])
    return True

  def contains(self, val)->bool:
    if val not in self.map:
      return False
    
    if val in self.map and self.map[val][-1][1] == False:
      return False
    
    return True

  def iterator(self):
    id = self.id
    self.id += 1
    return Iterator(self.arr, self.map, id, len(self.arr))
  
class Iterator:
  def __init__(self, arr, map, id, size) -> None:
    self.arr = arr
    self.map = map
    self.maxid = id  # max id number can use
    self.usedIdx = - 1
    self.maxsize = size

  def hasNext(self):
    next = self.nextIdx()
    # print('hasNext', res)
    if next == None :
      return False
    
    # print('hasNext is true', next)
    return True

  def next(self)->int:
    # print(self.usedIdx)
    next = self.nextIdx()
    if next == None :
      return None
    
    self.usedIdx = next
    return self.arr[next]
    
  def nextIdx(self)->int:
    nextIdx = self.usedIdx + 1
    while nextIdx < self.maxsize:
      val = self.arr[nextIdx]
      records = self.map[val] # [  [id1, True],  [id1, False] ....   ]
      # find larget id <= self.id
      index = bisect_right(records, self.maxid, key=lambda x: x[0] )
      if index > 0 and records[index - 1][1]:
        return nextIdx
      else: 
        nextIdx += 1
    
    return None
      

ss = SnapshotSet()
ss.add(5)
ss.add(8)
ss.add(2)

ss.remove(5)

it1 = ss.iterator()

print('it1')
while it1.hasNext():
  print(it1.next())  # 8, 2


ss.add(1)
ss.remove(2)

it2 = ss.iterator()
# print(it2.maxid, it2.maxsize)
print('it2')
while it2.hasNext():
  print(it2.next())  #  8, 1


if 1:
  print(1111)