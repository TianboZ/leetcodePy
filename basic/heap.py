import heapq
from heapq import heapify, heappop, heappush

'''
1. heapify is inplace operation
2. heappop returns top element

'''

# min heap
minHeap = [1,4,2,3,-100]
print('array, not heapified', minHeap)

heapq.heapify(minHeap)  # O(n)  
print('after heapify', minHeap )
print( 'minHeap type is ', type(minHeap)) # <class 'list'>

print('push -10000')
heapq.heappush(minHeap, -10000)  # O(log n)
print(minHeap)
print('access min heap smallest: ', minHeap[0])  # O(1)

min = heapq.heappop(minHeap)   # O(log n)
print(min)
print('min heap is', minHeap)

print('heap size: ', len(minHeap))  # O(1)

# max heap
maxHeap = [-n for n in [30, 10, -1, 100]]
print(maxHeap)

heapq.heapify(maxHeap)
while maxHeap:
  res = -heapq.heappop(maxHeap)
  print(res)
  pass


