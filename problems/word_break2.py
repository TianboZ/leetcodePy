class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    words = set(wordDict)
    self.res = []
    self.dfs(s, words, [])
    return self.res 
  
  def dfs(self, s, words, path):
    # baes case
    if not s:
      return

    # recursive rule
    if s in words:
      print(path + [s])
      word = list(path) + [s]
      word = ' '.join(word)
      self.res.append(word)
      # return

    for i in range(0, len(s) + 1):
      subStr = s[0: i]
      if subStr in words:
        path.append(subStr)
        self.dfs(s[i: len(s)], words, path)
        path.pop()