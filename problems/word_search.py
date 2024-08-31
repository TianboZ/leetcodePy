"""
solution:
- run depth limited DFS on the first matched letter 


complexity:
k is word length
board is m * n

DFS = O(branch ^ level) = O(4 ^ k)

time O(m * n * 4^k)
space O(k + m * n)

"""
from typing import List


DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
path = []
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.found = False
        visit = [[False for _ in range(n)] for _ in range(m)]  # Properly initialize visit array

        # traverse board
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    self.dfs(r, c, visit, board, 0, word)

        return self.found
    
    def dfs(self, x, y, visit, board, i, word):
        # base case
        if self.found:
            return
        
        if i == len(word) - 1:
            # found! 
            print(1111)
            self.found = True
            return
        
        # recursive rule
        visit[x][y] = True
        for dx, dy in DIRS:
            x2 = x + dx
            y2 = y + dy

            # when enter DFS, means next call is valid
            if self.isValid(x2, y2, board) and not visit[x2][y2] and board[x2][y2] == word[i + 1]:
                self.dfs(x2, y2, visit, board, i + 1, word)

        # backtracking
        visit[x][y] = False
    
    def isValid(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
        


sol  = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
res = sol.exist(board, "SEE")
print(res)