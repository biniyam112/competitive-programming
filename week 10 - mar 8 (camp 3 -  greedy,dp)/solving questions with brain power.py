from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        visited = {}
        def dp(index,points):
            if index >= len(questions):
                return points
            if index in visited:
                return visited[index]
            point1 = points + questions[index][0] + dp(index+questions[index][1]+1,points)
            point2 = points + dp(index+1,points)
            visited[index] = max(point1,point2)
            if point1 < point2:
                visited[index+1] = point2
            return max(point1,point2)
        return dp(0,0)