#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        from collections import deque
        row, col = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            while queue:
                x, y = queue.popleft()
                for dx, dy in dirs:
                    tmpX, tmpY = x+dx, y+dy
                    if 0<=tmpX<row and 0<=tmpY<col and board[tmpX][tmpY] == 'O':
                        board[tmpX][tmpY] = '#'
                        queue.append((tmpX, tmpY))
        
        for i in range(row):
            for j in range(col):
                if (i == 0 or j == 0 or i == row-1 or j == col-1) and board[i][j] == 'O':
                    board[i][j] = '#'
                    bfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

# @lc code=end

