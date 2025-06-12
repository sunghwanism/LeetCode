# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        newNode = ListNode(head.val)
        newTail = newNode
        current = head

        while current is not None:
            if newTail.val != current.val:
                newTail.next = ListNode(current.val)
                newTail = newTail.next
            current = current.next
        
        return newNode


        