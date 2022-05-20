class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]]+=1
            neighbors[pre[1]].append(pre[0])
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            for i in neighbors[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        if max(indegree) != 0:
            return False
        return True
        