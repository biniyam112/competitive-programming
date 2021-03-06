class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)