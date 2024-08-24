"""


"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        visit = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visit[i][j]:
                    self.bfs(i, j, visit, board)
        
    def bfs(self, i, j, visit, board):
        isRegionSurrounded = True
        queue = deque([])
        dirs = [[1, 0], [-1 , 0], [0, 1], [0, -1]]
        pos = [] # reocrd cordinates that are surrounded
        # init
        queue.append([i, j])
        visit[i][j] = True

        # terminate
        while queue:
            # expand 
            curr = queue.popleft()
            x, y = curr
            pos.append([x, y])
            if not self.isSurrounded(x, y, board):
                isRegionSurrounded = False

            # generate
            for dir in dirs:
                dx, dy = dir
                x2 = x + dx
                y2 = y + dy
                if self.isValid(x2, y2, board) and board[x2][y2] == 'O' and not visit[x2][y2]:
                    visit[x2][y2] = True
                    queue.append([x2, y2])
                    
        if isRegionSurrounded:
            for x, y in pos:
                board[x][y] = 'X'

    
    def isValid(self, i, j, board):
        m = len(board)
        n = len(board[0])

        return 0 <= i < m and 0 <= j < n
    
    def isSurrounded(self, i, j, board):
        m = len(board)
        n = len(board[0])

        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            return False
        
        return True
