class LazyArray: 
  def __init__(self, arr) -> None:
    self.arr = arr
    self.funcs = []
  
  def map(self, func)-> 'LazyArray':
    newLazy = LazyArray(self.arr)
    newFuncs = self.funcs.copy()
    newFuncs.append(func)
    newLazy.funcs = newFuncs
    return newLazy

  def indexOf(self, target):
    for idx, val in enumerate(self.arr):
      for func in self.funcs:
        val = func(val)
      if val == target:
        return idx

    return -1

# arr = LazyArray([10,20,30])

# res = arr.indexOf(20)
# print(res)

# arr2 = arr.map(lambda x: x+1)
# res = arr2.indexOf(11)
# print(res)

# res = arr.indexOf(20)
# print(res)

def test():

  arr = LazyArray([10,20,30])

  # test indexof
  assert arr.indexOf(10) == 0

  # test map
  arr2 = arr.map(lambda x:x+1).map(lambda x:x+1)
  assert arr2.indexOf(12) == 0

  # test LazyArry instance not affect each other
  assert arr.indexOf(10) == 0 and arr.indexOf(20) == 1 and arr.indexOf(30) == 2

  # test indexof when target not exist
  assert arr2.indexOf(100) == -1

  # test .map() not invoked if  .indexOf() not invoked yet
  arr3 = LazyArray([10,20,30])
  arr3 = arr3.map(lambda x:x+1)
  arr3 = arr3.map(lambda x:x+1)

  assert arr3.arr == [10, 20, 30]

test()

