# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    total = 0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def recursion(root,tilt):
            if not root:
                return 0
            right = recursion(root.right,tilt)
            left  = recursion(root.left,tilt)
            self.total += abs(right-left)
            return root.val +  right + left
        
        recursion(root,self.total)
        return self.total    