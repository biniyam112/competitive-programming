from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:     
        
        counter = 0
        # store index of visited
        visited = set()
        
        def dfs(row):
                visited.add(row)
                for col in range(len(isConnected)):
                    if col not in visited and isConnected[row][col] == 1 :
                        dfs(col)
            
        for row in range(len(isConnected)):
            if row not in visited:
                counter+=1
                dfs(row)
        return counter
        