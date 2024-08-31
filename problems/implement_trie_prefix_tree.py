class Node:
  def __init__(self, val = ""):
    self.isEnd = False
    self.val = val
    self.children = {} # <char: Node>

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, word: str) -> None:
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = Node(c)
      curr = curr.children[c]

    curr.isEnd  = True

  def search(self, word: str) -> bool:
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    
    print('search:', word, 'trie node:', curr.val)
    # check if the last char is end
    return curr.isEnd

  def startsWith(self, prefix: str) -> bool:
    curr = self.root
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    return True

  
  
# method 2
class Trie2:
  def __init__(self):
    # self.root = Node()
    self.isEnd = False
    self.children = {} # <char: Node>

  def insert(self, word: str) -> None:
    curr = self
    for c in word:
      if c not in curr.children:
        curr.children[c] = Trie2()   # inside class can refer to itself!!!
      curr = curr.children[c]
    
    curr.isEnd  = True

  def search(self, word: str) -> bool:
    curr = self
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    # check if the last char is end
    return curr.isEnd

  def startsWith(self, prefix: str) -> bool:
    curr = self
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    
    return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)