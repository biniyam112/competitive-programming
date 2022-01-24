    from typing import List


def spiralOrder(  matrix: List[List[int]]) -> List[int]:
        output = []
        steps = min(len(matrix),len(matrix[0]))
        for step in range(steps):
            i=step
            j=step
            # left to right - top
            if len(matrix[0]) - (2*step) <= 0:
                break
            while i < len(matrix[0])-step:
                output.append(matrix[j][i])
                i+=1
            i-=1
            # top to bottom - right side
            if len(matrix) - (2*step+1) <= 0:
                break
            j+=1
            if len(matrix) - 2* step <= 0:
                break
            while j < len(matrix)-step:
                output.append(matrix[j][i])
                j+=1
            j-=1
            # right to left -  bottom
            if len(matrix[0]) - (2*step+1) <= 0:
                break
            i-=1
            while i >= step :
                output.append(matrix[j][i])
                i-=1
            i+=1
            # bottom to top - left side
            if len(matrix) - (2*step+2) <= 0:
                break
            j-=1
            while j > step :
                output.append(matrix[j][i])
                j-=1
            j+=1
            i+=1
        return output
    
    
spiralOrder([[1,2,3,4],[5,6,7,8]])