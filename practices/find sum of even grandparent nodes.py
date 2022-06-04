# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def recursion(node,count):
            if not node:
                return 0
            left = 1 + recursion(node.left,count)
            right = 1 + recursion(node.right,count)
            if (left >= 3 or right >= 3) and node.val % 2 == 0:
                count[0] += node.val
            return max(left,right)
        count = [0]
        recursion(root,count)
        return count[0]