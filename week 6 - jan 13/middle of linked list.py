from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def middleNode( head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        temp = head
        while temp.next != None:
            temp = temp.next
            counter +=1
        counter +=1
        for i in range(counter//2):
            head = head.next
        return head
    
    