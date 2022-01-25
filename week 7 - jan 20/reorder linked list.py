

from importlib_metadata import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head
        fast = head
        slow = head
        temp = None
        while fast.next :
            temp = slow
            slow = slow.next
            fast = fast.next.next
            if not fast:
                break
        # slow is bigger or equal
        temp.next = None
        # reverse the slow pointer
        start = None
        while slow:
            temp = slow.next
            slow.next = start
            start = slow
            slow = temp
        temp =  head
        prev = None
        while head:
            var = head.next
            var2 = start.next
            start.next = var
            head.next = start
            # in case of odd length of nodes
            prev= head.next
            head = var
            start = var2
        prev.next = start
        # head = temp
        # print(temp)
            
            

            
        """
        Do not return anything, modify head in-place instead.
        """
        