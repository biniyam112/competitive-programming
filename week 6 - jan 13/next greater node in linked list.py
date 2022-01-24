from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    array =[]
    while head != None:
        array.append(head.val)
        head = head.next
    monostack = []
    removerdict = {}
    i = 0
    while i < len(array):
        if not monostack or array[i] < array[monostack[-1]] :
            monostack.append(i)
        while monostack and array[i] > array[monostack[-1]]:
            removerdict[monostack.pop()] = array[i]
        monostack.append(i)
        i+=1
    while monostack :
        removerdict[monostack.pop()] = 0
    removerdict = dict(sorted(removerdict.items()))
    return removerdict.values()
        
        