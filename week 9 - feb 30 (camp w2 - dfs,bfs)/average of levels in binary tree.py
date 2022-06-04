from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        queue = deque()
        queue.append(root)
        while queue or q2:
            total,counter= 0,0
            q2 = deque()
            while queue:
                node = queue.popleft()
                if node:
                    counter+=1
                    total += node.val
                    q2.append(node.left)
                    q2.append(node.right)
            if counter :
                output.append(total/counter)
            queue = q2
        return output
            
            
            
        
        