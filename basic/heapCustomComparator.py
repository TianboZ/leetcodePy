import heapq

print('------------------min heap----------------------------------')


# min heap
class Node(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __lt__(self, other):
    return self.a < other.a

  # def __repr__(self) -> str:
  #   return str(self.a)

n1 = Node(1, 2)
n2 = Node(100, 'sdf')
n3 = Node(-1, 100)
n4 = Node(3, 'fff')

pq = [n1, n2, n3, n4, Node(-2, 1)] # min heap

# print(len(pq))

heapq.heapify(pq)

while pq:
  res = heapq.heappop(pq)
  print(res.a)

print('------------------max heap----------------------------------')

# max heap
class Node2(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __lt__(self, other):
    return self.a > other.a


n1 = Node2(100, 1)
n2 = Node2(-1, 1)
n3 = Node2(-2, 1)
n4 = Node2(3, 1)
n5 = Node2(10, 1)
n6 = Node2(10, 12)

pq = [n1,n2,n3,n4,n5, n6]

heapq.heapify(pq)

while pq:
  res = heapq.heappop(pq)
  print(res.a)

