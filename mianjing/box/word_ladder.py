"""
complexity:
m is avg word length, n is words count

time: O(m * n^2)
space: O(m * n^2)
"""

from collections import defaultdict, deque
def solution(beginWord, endWord, words):
  words.append(beginWord)
  adj = getGraph(words)
  bfs(adj, beginWord, endWord)

def bfs(adj, beginWord, endWord):
  queue = deque([])
  visit = set()
  prev = {} # key: word, value: prev word
  
  # init
  queue.append(beginWord)
  visit.add(beginWord)
  
  while queue:
    # expand
    curr = queue.popleft()
    
    if curr == endWord:
      break
    
    # generate
    for next in adj.get(curr, []):
      if next not in visit:
        visit.add(next)
        queue.append(next)
        prev[next]=(curr)

  print('---')
  print(prev)
  
  if endWord in adj:
    curr = endWord
    path = []
    while curr:
      path.append(curr)
      curr = prev.get(curr, None)
    path.reverse()
    print(path)
  
def getGraph(words):
  adj = defaultdict(list)
  for w in words:
    for w2 in words:
      if w == w2:
        continue
      
      if len(w) != len(w2):
        continue
      
      # count how many chars are diff
      i = 0
      cnt = 0
      while i < len(w):
        c1 = w[i]
        c2 = w2[i]
        if c1 != c2:
          cnt += 1
        if cnt > 1:
          break
          
        i += 1
      
      if i == len(w) and cnt == 1:
        adj[w].append(w2)
  
  print(adj)  
  return adj

# test
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

solution(beginWord, endWord, wordList)