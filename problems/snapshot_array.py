"""

"""
from  sortedcontainers import SortedDict

class SnapshotArray:
  def __init__(self, length: int):
    self.arr = [SortedDict({0: 0}) for _ in range(length)] 
    self.id = 0
  
  def set(self, index: int, val: int) -> None:
    self.arr[index][self.id] = val
    
  def snap(self) -> int:
    self.id += 1
    return self.id - 1

  def get(self, index: int, snap_id: int) -> int:
    if index >= 0 and index < len(self.arr):
      sd: SortedDict= self.arr[index]
      snapIdIdx = sd.bisect_right(snap_id)
      if snapIdIdx > 0:
        snapIdIdx -= 1
        k, v = sd.peekitem(snapIdIdx)
        return v

    return 0


arr = SnapshotArray(3)
arr.set(0, 1)
arr.set(0, 2)
arr.set(0, 3)
arr.set(0, 4)
arr.snap()
val = arr.get(0, 1)
print(val)  # 4

for i in range(100):
  arr.snap()

val = arr.get(0, 90)
print(val)  # 4



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)