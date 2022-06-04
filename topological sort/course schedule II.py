from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        depend = defaultdict(list)
        
        for d,i in prerequisites:
            indegree[d]+=1
            depend[i].append(d)
            
        queue =  deque()
        for i,v in enumerate(indegree):
            if v == 0:
                queue.append(i)
                
        completed = []
        while queue:
            done = queue.popleft()
            completed.append(done)
            for item in depend[done]:
                indegree[item]-=1
                if indegree[item] == 0:
                    queue.append(item)
        if len(completed) == numCourses:
            return completed
        return []
        