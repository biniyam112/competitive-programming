# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_ptr = head
        for _ in range(left-1):
                left_ptr = left_ptr.next
        while right > left:
            right_ptr = head
            for _ in range(right-1):
                right_ptr = right_ptr.next
            left_ptr.val,right_ptr.val = right_ptr.val,left_ptr.val
            left_ptr = left_ptr.next
            left+=1
            right-=1
        return head
        