# Definition for a binary tree node.
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        maxvalue = -float('inf')
        queue = Deque()
        queue.append(root)
        counter  = 0
        length = (len(queue))
        while queue:
            node = queue.popleft()
            counter+=1
            maxvalue = max(maxvalue,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if counter == length:
                output.append(maxvalue)
                maxvalue = float('-inf')
                counter = 0
                length = len(queue)            
        return output
                
            
        