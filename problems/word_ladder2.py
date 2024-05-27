from collections import deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        if endWord not in wordList:
            return False

        adj = {}
        wordList.append(beginWord)
        res = []

        self.getGraph(adj, wordList)
        level = self.bfs(beginWord, endWord, adj)

        if level == 0:
            return res

        # depth limited DFS to find all path
        visit = set()
        path = []
        self.dfs(beginWord, endWord,adj, path, 0, level, visit, res)

        return res

    def dfs(self, node, end, adj, path: List[str], depth, maxDepth, visit: set[str], res):
        # base case
        if depth > maxDepth or node in visit:
            return

        # recursive rule
        visit.add(node)
        path.append(node)
        if node == end:
            copy = path.copy()
            res.append(copy)
        for nei in adj.get(node, []):
            self.dfs(nei, end, adj, path, depth + 1, maxDepth, visit, res)
        visit.remove(node)
        path.pop()


    def getGraph(self, adj, words: List[str]):
        wordsSet = set(words)
        for w in words:
            adj[w] = []
            arr = list(w)  # ['a', 'b', 'c']
            for i in range(len(arr)):
                oldChar = arr[i]
                for j in range(0, 26):
                    newChar = chr(97 + j)
                    if newChar != oldChar:
                        arr[i] = newChar
                        newWord = "".join(arr)
                        if newWord in wordsSet:
                            adj[w].append(newWord)
                arr[i] = oldChar

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
                    return level

                # generate
                for nei in adj.get(curr, []):
                    if nei not in visit:
                        visit.add(nei)
                        queue.append(nei)

            level += 1

        return 0

# test
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = sol.findLadders(beginWord, endWord, wordList)
print(res)