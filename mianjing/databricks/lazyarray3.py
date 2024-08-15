class LazyArray:
  def __init__(self, values, cbs=[]):
    self.values = values
    self.cbs = cbs

  # time O(n)
  def map(self, cb)->'LazyArray':
    return LazyArray(self.values,  cbs=self.cbs + [cb])
  
  # time O(n * m)  m is number of .map called
  def indexOf(self, target)->int:
    for i, val in enumerate(self.values):
      for cb in self.cbs:
        val = cb(val)
      if val == target:
        return i

    return -1
  
def test():
  arr = [10, 20, 30, 40]
  la = LazyArray(arr)

  # test indexOf
  assert la.indexOf(10) == 0

  la2 = la.map(lambda x: x + 1).map(lambda x: x + 1)

  # test arr field not affect if indexOf is not called
  assert la2.values == arr
  print(la2.values)

  # test indexOf, original instance not affected
  assert la.indexOf(10) == 0

  # chain of map
  print(la2.cbs)
  assert la2.indexOf(12) == 0

  # test not found
  assert la2.indexOf(100) == -1

  # verify original arr not affected
  assert arr == la.values

  print('la.cbs length', len(la.cbs))
  print('la.indexOf 10:' , la.indexOf(10))


  la3 = la.map(lambda x:x-1)
  print('la3:', la3.values, '  cbs length:', len(la3.cbs), la3.indexOf(9))
  assert la3.indexOf(9) == 0

test()