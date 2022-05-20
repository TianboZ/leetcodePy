class Solution(object):
  def permutations(self, input):
    """
    input: string input
    return: string[]
    """
    # write your solution here
    self.res = []
    list = [c for c in input]
    self.dfs(list, 0, input)
    print(self.res)
    return self.res

  def dfs(self, list, i, str):
    #  base case
    if i == len(str):
      tmp = ''.join(list)
      self.res.append(tmp)
      return

    # recursive rule
    for j in range(i, len(str)):
      self.swap(list, j, i)
      self.dfs(list, i + 1, str)
      self.swap(list, j, i)
  
  def swap(self, list, i, j):
    # print(list)
    # print('i:', i, 'j:', j)
    (list[i], list[j]) = (list[j], list[i])

sol = Solution()
sol.permutations('abc')