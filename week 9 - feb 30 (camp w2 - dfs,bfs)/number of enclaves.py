from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        output = 0
        def dfs(row,col):
            nonlocal counter,outofbound
            grid[row][col] = 0
            counter+=1
            for i in range(len(dirs)-1):
                new_row,new_col = row+dirs[i],col+dirs[i+1]
                if not inbound(new_row,new_col):
                    outofbound = True
                elif inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                    dfs(new_row,new_col)
        n,m = len(grid),len(grid[0])
        dirs =[1,0,-1,0,1]
        inbound = lambda row,col: 0 <= row < n and 0 <= col < m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 :
                    outofbound = False
                    counter = 0
                    dfs(i,j)
                    if not outofbound:
                        output += counter
        return output