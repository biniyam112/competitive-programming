from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        temp = head
        while head != None:
            array.append(head.val)
            head = head.next
        array = list(set(array))
        array.sort()
        if len(array) == 0:
            return head
        def createLinkedList(n):
            if n == len(array)-1:
                return ListNode(array[n])
            return ListNode(array[n],createLinkedList(n+1))
        return createLinkedList(0)