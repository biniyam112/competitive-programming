# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        reverse = False
        queue.append(root)
        counter = 0
        length = len(queue)
        output = []
        level = []
        if not root:
            return root
        while queue:
            node = queue.popleft()
            counter +=1
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if counter == length:
                counter = 0
                length = len(queue)
                if reverse:
                    level.reverse()
                output.append(level)
                reverse = not reverse
                level = []
        return output
        