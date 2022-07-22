# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodeList = []
        while head:
            nodeList.append(head.val)
            head= head.next
        lessList = []
        notLessList = []
        for i in nodeList:
            if i < x:
                lessList.append(i)
            else:
                notLessList.append(i)
        nodeList = lessList+notLessList
        node = ListNode()
        holder = node
        for i in nodeList:
            node.next = ListNode(i)
            node = node.next
        return holder.next
                
                
            