"""
# Definition for a Node.

"""

class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    map = {}
    return self.copy(head, map)

  # given head, return head of copied linked list head
  def copy(self, head, map: dict):
    # base case
    if not head:
      return None
    if head in map:
      return map.get(head)

    # recursive rule
    copyHead = Node(head.val)
    map[head] = copyHead

    copyHead.next = self.copy(head.next, map)
    copyHead.random = self.copy(head.random, map)

    return copyHead
    


sol = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3
n1.random = n3

copyHead = sol.copyRandomList(n1)
print(copyHead)