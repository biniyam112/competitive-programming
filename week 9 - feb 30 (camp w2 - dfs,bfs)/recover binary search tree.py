# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(node,arr):
            if node:
                inorder(node.left,arr)
                arr.append(node)
                inorder(node.right,arr)
        arr = []
        wrong = []
        inorder(root,arr)
        arr_copy = arr.copy()
        arr_copy.sort(key=lambda x: x.val)
        for i in range(len(arr)):
            if arr[i].val != arr_copy[i].val:
                wrong.append(arr[i])
            if len(wrong) == 2:
                break
        wrong[0].val,wrong[1].val = wrong[1].val,wrong[0].val
        """
        Do not return anything, modify root in-place instead.
        """
        