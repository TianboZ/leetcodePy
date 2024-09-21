from collections import defaultdict
import heapq

def minCost(buses, fares, start, end):
  if start == end:
    return 0
  
  # build graph
  adj = defaultdict(list)  # <stop_id: [bus_id, bus_id2,....]>
  for k, v in buses.items():
    for stopId in v:
      adj[stopId].append(k)
  
  print(adj)
  
  # sanity check
  if start not in adj:
    return -1
  
  # init minheap
  minheap = [] # record [[total cost, bus_id], ....]
  visit = {} # <bus_id, min cost>
  
  for busId in adj.get(start, []):
    heapq.heappush(minheap, [fares[busId], busId])
    visit[busId] = fares[busId]
  
  # print(minheap)
  
  while minheap:
    # expand 
    curr = heapq.heappop(minheap)
    fair1, busId1 = curr
    
    if end in buses[busId1]:
      # reach target stoop
      print(curr)
    
    # generate
    for stop in buses[busId1]:
      for busId2 in adj.get(stop, []):
        fair2 = fares[busId2]
        fairTotal  = fair1 + fair2
        if busId2 not in visit or fairTotal < visit[busId2]:
          visit[busId2] = fairTotal
          heapq.heappush(minheap, [fairTotal, busId2])
    
# test

# buses= {
#   1: [2, 5, 7],
#   2: [3, 6, 9],
#   3: [ 5, 6],
#   4: [5, 9]
# }
# fares = {
#   1: 1,
#   2: 1, 
#   3: 1,
#   4: 4
# }
# start = 5
# end = 9
  
  
  
  
  
# buses = {
#     1: [1, 2],
#     2: [2, 3],
#     3: [3, 4],
#     4: [4, 5]
# }
# fares = {
#     1: 1,
#     2: 1,
#     3: 1,
#     4: 1
# }
# start = 1
# end = 5


# buses = {
#     1: [1, 2, 3],
#     2: [3, 4, 5],
#     3: [1, 5]
# }
# fares = {
#     1: 2,
#     2: 3,
#     3: 5
# }
# start = 1
# end = 5
  
  
  
# buses = {
#     1: [1, 2, 3, 4],
#     2: [2, 5, 6],
#     3: [3, 7, 8],
#     4: [4, 9],
#     5: [6, 9],
#     6: [1, 9]
# }
# fares = {
#     1: 2,
#     2: 3,
#     3: 4,
#     4: 5,
#     5: 1,
#     6: 10
# }
# start = 1
# end = 9

buses = {
    1: [2, 5, 7],
    2: [3, 6, 9],
    3: [5, 6],
    4: [5, 9]
}
fares = {
    1: 1,
    2: 1, 
    3: 1,
    4: 4
}
start = 5
end = 9

minCost(buses, fares, start, end)
  