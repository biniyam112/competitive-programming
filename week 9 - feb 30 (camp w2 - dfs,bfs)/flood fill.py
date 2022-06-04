from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        isInBound  = lambda row,col : 0 <= row < len(image) and 0 <= col < len(image[0])
        dirs = [0,1,0,-1,0]
        
        def dfs(row,col):
            image[row][col] = newColor
            
            for i in range(4):
                new_row,new_col = row + dirs[i] , col + dirs[i+1]
                if not isInBound(new_row,new_col) or image[new_row][new_col] != targetColor:
                    continue
                dfs(new_row,new_col)
        
        
        if targetColor != newColor:
            dfs(sr,sc)
        return image