class Solution:
  # given [1,2,3,4], find length of 6 all combination, each num can use from 0 to 6 times
  def q1(self, nums, size):
    self.res = []
    self.dfs(nums, 0, size, [])
  
  def dfs(self, nums, i, size, path):
    # base case
    if i == size:
      print(''.join(path))
      return
    
    # recursive rule
    for n in nums:
      path.append(str(n))
      self.dfs(nums, i + 1, size, path)
      path.pop()
      
  def swap(self, i, j, nums):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    
  # each number used once, so size <= len(nums)    [1,2, 3, 4]  size = 3
  def q2(self, nums, size):
    res = []
    def dfs(i, nums, path, size, visit):
      # base case
      if i == size:
        print(''.join(path))
        res.append(''.join(path))
        return
      
      # recursive rule
      for n in nums:
        if n in visit:
          continue
        
        path.append(str(n))
        visit.add(n)
        dfs(i + 1, nums, path, size, visit)
        path.pop()
        visit.remove(n)
    
    visit = set()
    dfs(0, nums, [], size, visit)
    print('total:',len(set(res)))

sol = Solution()
sol.q1([1, 2, 3, 4], 5)
# sol.q2([1,2,3,4, 5], 3)

