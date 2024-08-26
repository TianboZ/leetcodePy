import heapq as hq
from typing import *
from UtilityClasses import *


class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ListNode.__lt__ = lambda self, other: self.val < other.val
    
    pq = [] # min heap
    dummy = ListNode(0)
    curr = dummy
    
    for node in lists:
      if node: hq.heappush(pq, node)
        
    while pq:
      node = hq.heappop(pq)
      curr.next = node
      curr = curr.next
      
      if node.next:
        hq.heappush(pq, node.next)
        
    return dummy.next
      
        
import heapq
class Node:
  def __init__(self, node):
    self.node = node

  def __lt__(self, other):
    return self.node.val < other.node.val

class Solution2:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    minheap = []
    dummy = ListNode(0)
    curr = dummy
    
    # init the heap
    for head in lists:
      if head:
        minheap.append(Node(head))
        
    heapq.heapify(minheap)

    # extract minimum node from heap 
    while minheap:
      node = heapq.heappop(minheap)
      node = node.node
      # print(node)
      if not node:
        continue
      
      curr.next = node
      curr = curr.next
      
      if node.next:
        heapq.heappush(minheap, Node(node.next))
    
    # print(res)
    return dummy.next

      