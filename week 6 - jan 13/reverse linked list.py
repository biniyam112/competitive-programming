from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
    array  = []
    temp = head
    if temp == None:
        return temp
    while temp.next != None:
        array.append(temp.val)
        temp = temp.next
    array.append(temp.val)
    temp = head
    temp.val = array[-1]
    for i in range(len(array)-1,-1,-1):
        head.val = array[i]
        head = head.next
    head = temp
    return head
        