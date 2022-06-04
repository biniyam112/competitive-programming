from collections import deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        occur = {}
        for i in range(len(arr)):
            if arr[i] not in occur:
                occur[arr[i]] =  [i]
            else:
                occur[arr[i]].append(i)
        inbound = lambda i : 0 <= i < len(arr)
        
        # set of value and index
        visited = set([0])
        queue = deque([(0,0)])
        
        counter = 0

        while queue:
            index,level = queue.popleft()
            if index == len(arr)-1:
                return level
            level +=1
            for val in occur[arr[index]]:
                if inbound(val) and val not in visited:
                    visited.add(val)
                    queue.append((val,level))
            for val in [index+1,index-1]:
                if inbound(val) and val not in visited:
                    visited.add(val)
                    queue.append((val,level))
            occur[arr[index]].clear()
                    
                
        
        