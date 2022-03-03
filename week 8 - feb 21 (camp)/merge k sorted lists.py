from typing import List
import heapq
from typing import Optional

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
      start = ListNode()
      temp = start
      while merged:
        temp.next = ListNode(heapq.heappop(merged))
        temp = temp.next
      return start.next
      