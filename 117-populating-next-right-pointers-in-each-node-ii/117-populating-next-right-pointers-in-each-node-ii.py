"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        row = [root]
        while row:
            new_row = []
            if len(row) > 1:
                for a, b in zip(row, row[1:]):
                    a.next = b
            for node in row:
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)
            row = new_row
        return root