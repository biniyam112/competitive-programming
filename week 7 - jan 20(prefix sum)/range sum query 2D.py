from typing import List


class NumMatrix:
    matrix = []
    def __init__(self, matrix: List[List[int]]):
        i = 0
        while i < len(matrix):
            j = 1
            while j < len(matrix[0]):
                matrix[i][j] += matrix[i][j-1]
                j+=1
            i+=1
        self.matrix = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output = 0
        for i in range(row1,row2+1):
            if col1 == 0:
                output += self.matrix[i][col2]
                continue
            output += self.matrix[i][col2]-self.matrix[i][col1-1]
        return output

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)