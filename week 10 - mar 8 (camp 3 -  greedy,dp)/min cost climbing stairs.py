from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = {}
        def climbing(index):
            if len(cost)-2 <= index:
                return cost[index]
            
            # dynamic part
            if index in visited:
                return visited[index]
            onestep = cost[index]+climbing(index+1)
            twosteps = cost[index]+climbing(index+2)
            
            if index not in visited:
                visited[index] = min(onestep,twosteps)
            return min(onestep,twosteps)
        return min(climbing(0),climbing(1))
        