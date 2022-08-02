class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0,1],[1,0]]
        inbound = lambda row , col : 0 <= row < m and 0 <= col < n
        visited = {}
        def dfs(row,col):
            if row == m-1 or col == n-1:
                return 1
            if (row,col) not in visited:
                value = 0
                for way in dirs:
                    new_row,new_col = row+way[0],col+way[1]  
                    if inbound(new_row,new_col):
                        value += dfs(new_row,new_col)
                visited[(row,col)] = value
            return visited[(row,col)]
        return dfs(0,0)
            
        