# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
map, key is depth, value is array of element
e.g.
{
  1: [2],
  2: [1,1,1,1,]
}
"""

class Solution:
  def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    self.maxDepth = 1
    map = collections.defaultdict(list)
    for child in nestedList:
      self.dfs(child, 1, map)
    
    # build ans
    res = 0
    print(map, self.maxDepth )
    for depth in map.keys():
      vals = map.get(depth)
      weight = self.maxDepth - depth + 1
      for v in vals:
        res += v * weight
    
    return res

  def dfs(self, node, depth, map):
    # baes case
    self.maxDepth = max(self.maxDepth, depth)
    
    # recursive rule
    num = node.getInteger()
    if num:
      # integer
      map[depth].append(num)
      
    else:
      # list
      for child in node.getList():
        self.dfs(child, depth + 1, map)

        