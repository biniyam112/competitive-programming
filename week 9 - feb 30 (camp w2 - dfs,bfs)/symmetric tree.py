# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            queue = deque()
            queue.append(root)
            while queue:
                for i in range(len(queue)//2):
                    if not queue[i]  and not queue[-i-1]:
                        continue
                    if (queue[i] and not queue[-i-1]) or (not queue[i] and queue[-i-1]) or queue[i].val != queue[-i-1].val:
                        return False
                temp = deque()
                while queue:
                    node = queue.popleft()
                    if node:
                        temp.append(node.left)
                        temp.append(node.right)
                queue = temp
            return True