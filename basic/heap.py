import heapq

# min heap
minHeap = [1,4,2,3,-100]
heapq.heapify(minHeap)  # O(n)
print('minHeap type is ', type(minHeap)) # list

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


