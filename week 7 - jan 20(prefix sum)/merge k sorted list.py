# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        heapq.heapify(merged)
        for i in lists:
            while i:
                heapq.heappush(merged,i.val)
                i = i.next
        start = temp = ListNode()
        while merged:
            temp.next = ListNode(heapq.heappop(merged))
            temp = temp.next
        return start.next
      
        
        
# Time limit exceeded
        # start = ListNode()
        # pointer = start
        # counter = 0
        # while counter < len(lists):
        #     least = 0
        #     counter = 0
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             counter+=1
        #         elif not lists[least] or lists[i].val < lists[least].val:
        #             least = i
        #     if lists[least]:
        #         start.next = ListNode(lists[least].val)
        #         lists[least] = lists[least].next
        #         start = start.next
        # return pointer.next
                