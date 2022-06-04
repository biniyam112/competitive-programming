from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        inbound = lambda index : 0 <= index < len(arr)
        queue = deque()
        queue.append(start)
        while queue:
            index = queue.popleft()
            visited.add(index)
            if arr[index] == 0:
                return True
            right = index+arr[index]
            left = index-arr[index]
            if inbound(right) and right not in visited:  
                queue.append(right)
            if inbound(left) and left not in visited:
                queue.append(left)
        return False
                