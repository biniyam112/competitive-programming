class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def helper(i, j, score):
            if i == m or j == n:
                return False
            if i == m - 1 and j == n - 1:
                return score == 1 and grid[i][j] == ')'
            
            if grid[i][j] == '(':
                return helper(i + 1, j, score + 1) or helper(i, j + 1, score + 1)
            if score == 0:
                return False
            return helper(i + 1, j, score - 1) or helper(i, j + 1, score - 1)
        
        return helper(0, 0, 0)