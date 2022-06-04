from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        directions = [1,0,-1,0,1]
        inbound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row,col):
            nonlocal area,maxarea,directions,inbound
            grid[row][col] = 0
            area+=1
            for i in range(len(directions)-1):
                new_row,new_col = row+directions[i],col+directions[i+1]
                if inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                    dfs(new_row,new_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    maxarea = max(maxarea,area)
        return maxarea