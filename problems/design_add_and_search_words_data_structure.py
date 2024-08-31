class Trie:
  def __init__(self):
    self.isEnd = False
    self.neis = {}

  def add(self, word):
    curr = self
    for c in word:
      if c not in curr.neis:
        curr.neis[c] = Trie()
      curr = curr.neis[c]
    curr.isEnd = True
  
class WordDictionary:
  def __init__(self):
    self.trie = Trie()

  def addWord(self, word: str) -> None:
    self.trie.add(word)

  def search(self, word: str) -> bool:
    root = self.trie
    return self.dfs(root, 0, word)
  
  # return True if find match
  def dfs(self, node, i, word)->bool:
    # baes case
    if i == len(word):
      return node.isEnd

    # recursive rule
    c = word[i]
    if c == '.':
      # wildcard
      for nei in node.neis.values():
        if self.dfs(nei, i + 1, word):
          return True
    else:
      if c not in node.neis:
        return False

      node = node.neis[c]
      if self.dfs(node, i + 1, word):
        return True
    
    return False

    
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)