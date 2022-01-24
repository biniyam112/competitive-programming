class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        temp = newhead
        while head != None:
            if head.next == None:
                newhead.next = head
                head = head.next
            else:
                newhead.next = ListNode(head.next.val)
                newhead = newhead.next
                newhead.next = ListNode(head.val)
                newhead = newhead.next
                head = head.next.next
        return temp.next