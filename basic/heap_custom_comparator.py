'''

https://www.geeksforgeeks.org/heapq-with-custom-predicate-in-python/


'''

import heapq

print('------------------min heap----------------------------------')


# min heap
class MinNode(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __lt__(self, other):
    return self.a < other.a

n1 = MinNode(1, 2)
n2 = MinNode(100, 'sdf')
n3 = MinNode(-1, 100)
n4 = MinNode(3, 'fff')

pq = [n1, n2, n3, n4, MinNode(-2, 1)] # min heap

# print(len(pq))

heapq.heapify(pq)

while pq:
  res = heapq.heappop(pq)
  print(res.a)

print('------------------max heap----------------------------------')

# max heap
class MaxNode(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __lt__(self, other):
    return self.a > other.a


n1 = MaxNode(100, 1)
n2 = MaxNode(-1, 1)
n3 = MaxNode(-2, 1)
n4 = MaxNode(3, 1)
n5 = MaxNode(10, 1)
n6 = MaxNode(10, 12)

pq = [n1,n2,n3,n4,n5, n6]

heapq.heapify(pq)

while pq:
  res = heapq.heappop(pq)
  print(res.a)

