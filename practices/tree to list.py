from typing import List



class Node:

    def __init__(self,val:int):
        self.val = val
        self.right = self.left = None



    def treeToList(self,root,arr:List[int]):
        if  not root:
            return arr
        self.treeToList(root.right)
        arr.append(root.val)
        self.treeToList(root.left)