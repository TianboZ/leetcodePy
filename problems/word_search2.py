from typing import List


class Node:
  def __init__(self, val =""):
    self.val = val
    self.neis = {} # <char, Node>
    self.isEnd = False

class Trie:
  def __init__(self):
    self.root = Node()
  
  def addWord(self, word):
    curr = self.root
    for c in word:
      if c not in curr.neis:
        curr.neis[c] = Node(c)
      curr = curr.neis[c]
    curr.isEnd = True

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # init Trie 
    trie = Trie()
    root = trie.root

    # add word to trie
    for word in words:
      trie.addWord(word)

    # traverse board
    self.res = []
    m = len(board)
    n = len(board[0])
    for i in range(m):
      for j in range(n):
        visit = [[False for _ in range(n)] for _ in range(m)]
        path = []
        self.dfs(i, j, visit, board, path, root)

    return list(set(self.res))

  # path: record path ['a', 't', ...]
  # node: trie node
  def dfs(self, i, j, visit, board, path, node):
    # baes case 
 
    
    # recursive rule
    c = board[i][j]
    
    if c not in node.neis:
      return
    
    visit[i][j] = True
    node = node.neis[c]    
    path.append(c)

    if node.isEnd:
      # find valid word
      self.res.append(''.join(path))
      print(path)

    for dir in [[0,1], [0, -1], [1, 0], [-1, 0]]:
      dx, dy = dir
      x = i + dx
      y = j + dy
      if self.isValid(x, y, board) and not visit[x][y]:
        self.dfs(x, y, visit, board, path, node)

    visit[i][j] = False
    path.pop()
  
  def isValid(self, i, j, board):
    return 0 <= i < len(board) and 0 <= j < len(board[0])
  
  
sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
board2 = [
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"],
  ["a","a","a","a","a","a","a","a","a","a","a","a"]
]
words = ['oath', 'lv', 'aaaaaaaaaaaaaaaaaaaaa']
sol.findWords(board, words)