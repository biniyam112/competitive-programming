from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        decimal = 0
        while l1 != None and l2 != None:
            array.append((l1.val+l2.val+decimal)%10)
            decimal = (l1.val+l2.val+decimal)//10
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            array.append((l1.val+decimal)%10)
            decimal = (l1.val+decimal)//10
            l1 = l1.next
        while l2 != None:
            array.append((l2.val+decimal)%10)
            decimal = (l2.val+decimal)//10
            l2 = l2.next
        if decimal >0:
            array.append(decimal)
        def createLinkedList(n):
            if n == len(array)-1:
                return ListNode(array[n])
            return ListNode(array[n],createLinkedList(n+1))
        head = createLinkedList(0)
        return head
            
            
        