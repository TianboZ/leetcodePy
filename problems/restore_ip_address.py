class Solution(object):
  def Restore(self, ip):
    """
    input: string ip
    return: string[]
    """
    # write your solution here
    self.res = []
    self.dfs([], 0, 0, ip)
    return self.res  

  # i: ip string, from index to process
  # level: recursive depth
  def dfs(self, path, i, depth, ip):
    # base case
    if depth == 4 or i == len(ip):
      # print(path, 'i', i, 'depth', depth)
      if i == len(ip) and len(path) == 4:
        res = [str(x) for x in path]
        self.res.append('.'.join(res))
      return 

    # recursive rule
    size = len(ip)
    
    # 1 digit
    num = int(ip[i: i + 1])
    path.append(num)
    self.dfs(path, i + 1, depth + 1, ip)
    path.pop()
  
    # 2 digits
    if i + 1 < size:
      num = int(ip[i: i + 2])
      if num >= 10:
        path.append(num)
        self.dfs(path, i + 2, depth + 1, ip)
        path.pop()

    # 3 digits
    if i + 2 < size:
      num = int(ip[i: i + 3])
      if num >= 100 and num <= 255:
        path.append(num)
        self.dfs(path, i + 3, depth + 1, ip)
        path.pop()   


sol = Solution()
res = sol.Restore('0022310')
print(res)