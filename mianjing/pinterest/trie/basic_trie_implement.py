from sys import prefix


class Node:
  def __init__(self, c, isEnd = False):
    self.char = c
    self.isEnd = isEnd
    self.children = {} # <char, Node>

class Trie:
  def __init__(self):
    self.root = Node('')

  def insert(self, word: str) -> None:
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = Node(c)
      curr = curr.children[c]
    curr.isEnd = True
      

  def search(self, word: str) -> bool:
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return curr.isEnd

  def startsWith(self, prefix: str) -> bool:
    curr = self.root
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return True

        
# init
trie = Trie()

# word
word = 'abc def ggd'
trie.insert(word)
print(trie.search(word))

prefix = 'abc d'
print(trie.startsWith(prefix))

# ips
trie.insert('1.1.1.1')
trie.insert('1.1.1.2')
trie.insert('1.1.1.33')
trie.insert('1.1.2.56')
print(trie.startsWith('1.1.2.'))
print(trie.search('1.1.2.'))