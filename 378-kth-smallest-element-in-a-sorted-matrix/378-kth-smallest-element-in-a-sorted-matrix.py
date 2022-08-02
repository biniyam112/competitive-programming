class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        indexes = [0] * len(matrix)
        i = 0
        while i < k:
            minval = float('inf')
            minindex = 0
            for j in range(len(matrix)):
                if indexes[j] < len(matrix) and matrix[j][indexes[j]] < minval:
                    minval = matrix[j][indexes[j]]
                    minindex = j
            indexes[minindex] += 1
            i+=1
            if i == k:
                return minval
        
        