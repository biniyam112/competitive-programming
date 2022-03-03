# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      node = None
      def recursion(head,node):
        if not head:
          return node
        temp = head.next
        head.next = node
        node = head
        head = temp
        return recursion(head,node)
      return recursion(head,node)