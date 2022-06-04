from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        done = set()
        directions = [1,0,-1,0,1]
        inbound = lambda row,col: 0 <= row < len(board) and 0 <= col < len(board[0])
        def dfs(row,col):
            nonlocal accept,directions,visited,inbound
            visited.add((row,col))
            done.add((row,col))
            for i in range(len(directions)-1):
                new_row,new_col = row+directions[i],col+directions[i+1]
                if inbound(new_row,new_col) and board[new_row][new_col] == 'O' and (new_row,new_col) not in done:
                    dfs(new_row,new_col)
                elif not inbound(new_row,new_col) and board[row][col] == 'O':
                    accept = False
        def change(visited):
            for r,c in visited:
                board[r][c] = 'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in done:
                    visited = set()
                    accept = True
                    dfs(i,j)
                    if accept:
                        change(visited)
                    
        """
        Do not return anything, modify board in-place instead.
        """
        