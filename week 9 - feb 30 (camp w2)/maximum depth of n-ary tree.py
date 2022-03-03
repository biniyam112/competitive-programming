
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        def recursion(root):
            if root.children == None:
                return 0
            else:   
                output =[0]
                for child in root.children:
                    output.append(1+recursion(child))
                return max(output)
        return 1+recursion(root)
        