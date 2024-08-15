class LazyArray:
  def __init__(self, arr: list[int]) -> None:
    self.arr = arr
    self.cbs = []

  # time O(n) 
  def map(self, cb) ->'LazyArray':
    newCbs = self.cbs.copy()
    newCbs.append(cb)
    newLa = LazyArray(self.arr)
    newLa.cbs = newCbs
    return newLa
  
  # time complexity: O(n * m)    n=array length   m = # of .map  
  def indexOf(self, x):
    for i in range(len(self.arr)):
      val = self.arr[i]
      
      if val == x:
        return i
      
      for cb in self.cbs:
        if cb:
          val = cb(val)
        
      if val == x:
        return i  
    
    return -1
  


def testLazyArray():
  # Test without any transformation
  la = LazyArray([1, 2, 3, 4])
  assert la.indexOf(3) == 2
  print(la.indexOf(3))

  # Test with a single transformation
  la = LazyArray([1, 2, 3, 4])
  la2 = la.map(lambda x: x * 2)
  assert la.indexOf(6) == -1 # verify original object is not affected
  assert la2.indexOf(6) == 2

  # Test with multiple transformations
  la = LazyArray([1, 2, 3, 4])
  la2 = la.map(lambda x: x + 10) # verify objects not affect each other
  la3 = la.map(lambda x: x * 2)
  print(la3.arr, la3.indexOf(8))
  assert la3.indexOf(8) == 3

  # Test for element not found
  la = LazyArray([1, 2, 3, 4])
  assert la.indexOf(10) == -1

  # test lazy: .map() not applied to array item  if no .indexOf called
  la2 = la.map(lambda x: x+1).map(lambda x: x+1)  
  assert la.arr == la2.arr  
  print(la.arr)

  print("All tests passed!")

# Run the tests
testLazyArray()


lazy = LazyArray([10, 20, 30])
lazy2 = lazy.map(lambda x: x+1).map(lambda x: x + 1)
lazy3 = lazy.map(lambda x: x+3)

print(lazy.indexOf(20), lazy2.indexOf(32), lazy3.indexOf(23))



