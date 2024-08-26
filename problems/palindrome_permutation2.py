"""
solution:
- only generte 1st half, 2nd half just the reverse
- count char frequncy, if more than one char that is odd freq, not possible palindrome
"""
import collections
class Solution:
  def generatePalindromes(self, s: str) -> List[str]:
    map = collections.Counter(s)
    print(map)
    oddCnt = 0
    oddStr = ''
    chars = []
    for k in map.keys():
      freq = map.get(k)
      if freq % 2 != 0:
        # build odd substring
        for _ in range(freq // 2):
          chars.append(k)
        oddStr = k
        
        # invalid palindrome
        oddCnt += 1
        if oddCnt > 1:
          return []
      else:
        for _ in range(freq // 2):
          chars.append(k)
    print(chars)  # e.g. [a, b]

    # build res
    res = []
    chars.sort()
    self.dfs(chars, 0, res, oddStr)
    
    return list(res)
    
  # permutation 
  def dfs(self, arr, i, res, oddStr):
    # baes case
    if i == len(arr):
      leftStr = ''.join(arr)
      rightStr = leftStr[::-1]
      res.append(leftStr + oddStr + rightStr)    
      # print(res)
      return

    # recursive rule
    j = i
    visit = set()
    for j in range(i, len(arr)):
      # skip same char
      if arr[j] in visit:
        continue
      
      visit.add(arr[j])
      self.swap(i, j, arr)
      self.dfs(arr, i + 1, res, oddStr)
      self.swap(i, j, arr)

  def swap(self,  i, j, arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
