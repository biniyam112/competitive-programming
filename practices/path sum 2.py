# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output = []
        def recursion(root,total,nodes):
            if not root:
                return 0
            nodes = [x for x in nodes]
            total += root.val
            nodes.append(root.val)
            if not root.left and not root.right:
                if total == targetSum:
                    self.output.append(nodes)
            if root.right:
                recursion(root.right,total,nodes)
            if root.left:
                recursion(root.left,total,nodes)
        
        recursion(root,0,[])
        return self.output