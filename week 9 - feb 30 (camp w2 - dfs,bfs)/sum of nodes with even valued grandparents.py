# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.count = 0
        def recursion(child,parent,gp,counter):
            if not child:
                return
            counter +=1
            if counter > 2 and gp.val % 2 == 0 :
                self.count += child.val
            gp = parent
            parent = child
            recursion(child.left,parent,gp,counter)
            recursion(child.right,parent,gp,counter)
        recursion(root,root,root,0)
        return self.count