from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        output = {}
        visited = set()
        final = []
        def dfs(index):
            if index in output:
                return output[index]
            if index in visited:
                return False
            if not graph[index]:
                return True
            visited.add(index)
            for i in graph[index]:      
                x = output[i] if i in output else dfs(i)
                if not x:
                    output[index] = False
                    return False
            visited.remove(index)
            output[index] = True
            return True
        for i in range(len(graph)):
            if dfs(i):
                final.append(i)
        final.sort()
        return final
                