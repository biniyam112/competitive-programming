from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TLE
        # insertion = [head]
        # while head.next != None:
        #     head = head.next
        #     insertion.append(head)
        #     i = len(insertion)-1
        #     temp = insertion[-1].val
        #     while i > 0 and insertion[i-1].val > temp:
        #         insertion[i].val = insertion[i-1].val 
        #         i-=1
        #     insertion[i].val = temp
        # return insertion[0]
        
        sortedhead = ListNode(head.val)
        print(sortedhead)
        print('outside-=-=-=-=-=-=-=-=-=-=-=')
        temp = sortedhead
        while head.next != None:
            head = head.next
            if sortedhead.val > head.val:
                sortedhead = ListNode(head.val,sortedhead)
                temp = sortedhead
                # print(sortedhead)
                # print('prepend================')
            else:
                while sortedhead.next != None and sortedhead.next.val < head.val:
                    sortedhead = sortedhead.next
                if sortedhead.next == None:
                    sortedhead.next = ListNode(head.val)
                    # print(sortedhead)
                    # print('append last-------------------')
                else:
                    val = sortedhead.next
                    sortedhead.next = ListNode(head.val)
                    sortedhead.next.next = val
                    # print(sortedhead)
                    # print('append middle---------------')
            sortedhead = temp
        return sortedhead
            
    
    
    
        
                    
            
        
        