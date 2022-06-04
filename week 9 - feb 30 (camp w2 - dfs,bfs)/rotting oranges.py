from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [0,1,0,-1,0]
        queue = deque()
        n,m = len(grid),len(grid[0])
        inbound = lambda row,col : 0 <= row < n and 0 <= col < m
        zeros = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zeros+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        if zeros == m*n:
            return 0
        output = 0
        counter = 0
        length = len(queue)
        
        while queue:
            counter +=1
            row,col = queue.popleft()
            for i in range(len(directions)-1):
                new_row,new_col = row+directions[i],col+directions[i+1]
                if inbound(new_row,new_col) and grid[new_row][new_col] == 1 :
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col))
            if counter == length:
                output +=1
                counter = 0
                length = len(queue)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return output-1