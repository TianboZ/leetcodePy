class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class GraphNode(object):
  def __init__(self, val):
    self.val = val
    self.nodes = []


class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []