from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    array = []
    if list1 == None :
        return list2
    if list2 == None:
        return list1
    while list1.next != None:
        array.append(list1.val)
        list1 = list1.next
    array.append(list1.val)
    while list2.next != None:
        array.append(list2.val)
        list2 = list2.next
    array.append(list2.val)
    array.sort()
    def createLinkedList(n):
        if n == len(array)-1:
            return ListNode(array[n])
        return ListNode(array[n],createLinkedList(n+1))
    return createLinkedList(0)