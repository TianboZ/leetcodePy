# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# 我被 linkedin 靠了，现场做出来了！ on 9/3/24
class NestedIterator:
  def __init__(self, nestedList: [NestedInteger]):
    self.res = []
    self.i = 0
    
    def dfs(nestedArr):
      # case case
      if not nestedArr:
        return 

      # recursive rule 
      for ele in nestedArr:
        num = ele.getInteger()
        nums = ele.getList()
        if num or num == 0:
          self.res.append(num)
        elif nums:
          dfs(nums)

    dfs(nestedList) # get flatten array [1, 2, 3, 3, 4]
  
  def next(self) -> int:
    num = self.res[self.i]
    self.i += 1
    return num
  
  def hasNext(self) -> bool:
    return self.i < len(self.res) 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())