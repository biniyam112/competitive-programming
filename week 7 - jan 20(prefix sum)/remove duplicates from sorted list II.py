from async_timeout import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head or not head.next:
        return head
      dummy = ListNode(float('inf'),head)
      head = dummy
      start = head
      end = head.next
      while end and end.next:
        if start.val == end.val:
          while start.val == end.val:
            end = end.next
            if not end:
              break
          if prev == None:
            start.next = end
          else:
            prev.next = end
          start = prev
        else:
          prev = start
          start = start.next
          end = end.next
      if not end and start.val == float('inf'):
        return None
      if end and start.val == end.val:
        prev.next = None
      return dummy.next
          
        