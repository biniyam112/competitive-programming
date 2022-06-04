# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        temp = newhead
        while list1 or list2:
            if not list1:
                newhead.next = list2
                return temp.next
            if not list2:
                newhead.next = list1
                return temp.next
            if list1.val <= list2.val:
                newhead.next = ListNode(list1.val)
                newhead = newhead.next
                list1 = list1.next
            else:
                newhead.next = ListNode(list2.val)
                newhead = newhead.next
                list2 = list2.next
        return temp.next