# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        output = {}
        def inorder(node,level):
            if not node.right and not node.left:
                if level in output:
                    output[level] += node.val
                else:
                    output[level] = node.val
                return
            if node.right:
                inorder(node.right,level+1)
            if node.left:
                inorder(node.left,level+1)
        inorder(root,0)
        deepest  = [0,0]
        for k,v in output.items():
            if k > deepest[0]:
                deepest[0] = k
                deepest[1] = v
        return deepest[1]
        
        