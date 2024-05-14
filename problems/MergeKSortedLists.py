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
      
        
      