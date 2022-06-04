# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (None,0)
                
            right = dfs(node.right)
            left  = dfs(node.left)
            if right[1] > left[1]:
                return (right[0],right[1]+1)
            elif right[1] < left[1]:
                return (left[0],left[1]+1)
            else:
                return (node,right[1]+1) 

        return dfs(root)[0]