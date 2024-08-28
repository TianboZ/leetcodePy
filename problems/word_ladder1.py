from collections import deque
from typing import List

'''
solution:
1. build map, <work, array of 1 char diff words>
2. run BFS for begin word

complexity:
M = word length
N = # of words

- time:
build graph: O(26 * M * N) 
BFS: O(V + E) = O(N * M)

- space:
build graph: O(N * M)
BFS: O(V) = O(N * M)

'''
class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if  endWord not in wordList: 
      return False

    adj = {}
    wordList.append(beginWord)
    self.getGraph(adj, wordList)
    print(adj)
    
    return self.bfs(beginWord, endWord, adj)
  
  def getGraph(self, adj, words: List[str]):
    wordsSet = set(words)
    for w in words:
      adj[w] = []
      arr = list(w) # ['a', 'b', 'c']
      print(arr)
      for i in range(len(arr)):
        oldChar = arr[i]
        for j in range(0, 26):
          newChar = chr(97 + j)
          if newChar != oldChar:
            arr[i] = newChar
            newWord = "".join(arr)
            print('newWord=', newWord)
            if newWord in wordsSet:
              adj[w].append(newWord)
        arr[i] =oldChar


  def bfs(self, node, target, adj):
    queue = deque([])
    visit = set()
    level = 0
    # initial
    queue.append(node)
    visit.add(node)

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()
        if curr == target:
          return level + 1 #    # of words = level + 1
        
        # generate
        for nei in adj.get(curr, []):
          if nei not in visit:
            visit.add(nei)
            queue.append(nei)

      level += 1
    
    return 0  


"""
complexity:
n is word list length, m is word avg length

time: 
build adj graph = O(m * n * n) = O(n^2 * m)
bfs = O(V + E) = O(n)

total O(n + m*n^2) = O(m * n^2)

"""

import collections
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(set)
        self.getAdj(beginWord, endWord, wordList, adj)
        print(adj)    
        
        res = self.bfs(adj,beginWord, endWord)
        return res
    
    
    def getAdj(self, begin, end, words, adj):
        words.insert(0, begin)
        for w in words:
            for w2 in words:
                if w == w2:
                    continue
                if self.isOneCharDiff(w, w2):
                    adj[w].add(w2)
                    adj[w2].add(w)
        
        
    def bfs(self, adj, start, target):
        queue = deque([])
        visit = set()
        dis = 0
        
        # init
        queue.append(start)
        visit.add(start)
        
        
        #  terminate
        while queue:
            size = len(queue)
            for _ in range(size):
                #   expand
                curr = queue.popleft()
                
                if curr == target:
                    return dis + 1
                    print(dis)
                
                # generate
                for nei in adj.get(curr, []):
                    if nei not in visit:
                        queue.append(nei)
                        visit.add(nei)
            dis += 1
        
        return 0
                
        
    def isOneCharDiff(self, s1, s2):
        if len(s1) != len(s2):
            return False
        cnt = 0
        # print(s1)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return True
sol = Solution2()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = sol.ladderLength(beginWord, endWord, wordList)
print(res)

