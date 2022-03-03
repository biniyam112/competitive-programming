
from tkinter.tix import ListNoteBook
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNoteBook], n: int) -> Optional[ListNode]:
        temp  = head
        counter = 0
        while temp.next != None:
            counter+=1
            temp = temp.next
        counter += 1
        counter -= n
        print(counter)
        temp = head
        if counter ==0:
            head = head.next
            return head
        for _ in range(1,counter):
            head  = head.next
        if head.next != None:
            head.next = head.next.next
        else:
            temp = temp.next
        head = temp
        return head
        
        
removeNthFromEnd([ListNode(12,next=1),ListNode(1,next = 2),ListNode(5,next= 8),ListNode(8)],2)