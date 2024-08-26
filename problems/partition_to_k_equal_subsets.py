"""
naive solution:

complexity:
time O(branch ^ level) = O(n ^ n)


soluiton 2:

complexity:
timne O( 2^(k*n))
still TLE, but i think good enouth

"""
from typing import List


class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    self.target = sum(nums) / k
    self.cnt = 0
    taken = [False for _ in nums]
    self.res = False
    
    print(self.target)
    nums.sort(reverse=True)
    self.dfs(nums, k, 0,taken, 0)
    
    return self.res
  
  # taken: [true, false,...] for each item in nums,mark it used or not
  # cnt is number of subset
  def dfs(self, nums, k, cnt, taken, prevSum):
    # base case
    if self.res:
      return

    if cnt == k - 1:
      self.res = True
      return 
    
    # recursive rule
    for i in range(len(nums)):
      num = nums[i]
      if taken[i]:
        # used num
        continue

      newSum = prevSum + num
      # print('newSum', newSum)
      if newSum < self.target:
        taken[i] = True
        self.dfs(nums, k, cnt, taken, newSum)
        taken[i] = False
      
      if newSum == self.target:
        taken[i] = True
        self.dfs(nums, k, cnt + 1, taken, 0)
        taken[i] = False


class Solution2:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    self.target = sum(nums) / k
    self.cnt = 0
    self.taken = [False for _ in nums]
    self.res = False
    self.k = k
    
    # print(self.target)
    nums.sort(reverse=True)
    self.dfs(nums, 0, 0, 0)
    
    return self.res
  
  # taken: [true, false,...] for each item in nums,mark it used or not
  # cnt is number of subset
  def dfs(self, nums, i, cnt, prevSum):
    # base case
    if self.res:
      return

    if prevSum == self.target:
      self.dfs(nums, 0, cnt + 1, 0)
      return

    if cnt == self.k - 1:
      self.res = True
      return 
      
    if i == len(nums):
      return
    
    # recursive rule
    num = nums[i]
    # case 1, use num
    if not self.taken[i]:
      currSum = prevSum + num
      if currSum <= self.target:
        self.taken[i] = True
        self.dfs(nums, i + 1, cnt, currSum)
        self.taken[i] = False
    
    # case 2, not use num
    self.dfs(nums, i + 1, cnt, prevSum)
