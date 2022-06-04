# Definition for a binary tree node.
from typing import Optional
from typing import Optional

class TreeNode:



    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.output = False
        if not root:
            return False
        def recursion(root,val,target):
            val += root.val
            if root.left:
                recursion(root.left,val,target)
            if root.right:
                recursion(root.right,val,target)
            if not (root.right or root.left):
                self.output = self.output or val == target
                return
        recursion(root,0,targetSum)
        return self.output