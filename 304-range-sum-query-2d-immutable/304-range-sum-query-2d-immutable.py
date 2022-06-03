class NumMatrix:
    matrix = []
    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1,row2+1):
            if col1 > 0:
                total += self.matrix[i][col2]-self.matrix[i][col1-1]
            else:
                total += self.matrix[i][col2]
        return total
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)