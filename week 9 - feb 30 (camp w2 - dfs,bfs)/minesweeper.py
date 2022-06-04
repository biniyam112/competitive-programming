from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        
        DIR = [[1,1],[1,0],[1,-1],[0,-1],[-1,0],[-1,-1],[-1,1],[0,1]]
        def inBound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def dfs(row,col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return 
            bombcount = 0
            for d in DIR:
                new_row,new_col = row + d[0] , col + d[1]
                if inBound(new_row,new_col):
                    if board[new_row][new_col] == 'M':
                        bombcount+=1
            if bombcount == 0:
                board[row][col] = 'B' 
                for d in DIR:
                    new_row,new_col = row + d[0] , col + d[1]
                    if  inBound(new_row,new_col) and board[new_row][new_col] == 'E':
                        dfs(new_row,new_col)
            else:
                board[row][col] = str(bombcount)
        
        dfs(click[0],click[1])
        return board