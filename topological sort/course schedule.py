from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        depend = defaultdict(list)
        
        for d,i in prerequisites:
            indegree[d]+=1
            depend[i].append(d)
        
        queue = deque()
        for i,v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        
        
        counter = 0
        while queue:
            done = queue.pop()
            counter += 1
            if done in depend:
                for item in depend[done]:
                    indegree[item] -= 1
                    if indegree[item] == 0:
                        queue.append(item)
        return numCourses == counter
        
        