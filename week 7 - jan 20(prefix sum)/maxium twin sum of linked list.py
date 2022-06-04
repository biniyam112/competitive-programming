from async_timeout import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        temp = None
        while fast.next != None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            if fast == None:
                break
        temp.next = None
        # slow is head of second half
        # reverse slow
        start = None
        while slow:
            var = slow.next
            slow.next = start
            start = slow
            slow = var
        output = 0
        while head:
            output = max(output,start.val + head.val)
            start = start.next
            head = head.next
        return output