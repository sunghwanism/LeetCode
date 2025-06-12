# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        newNode = ListNode()
        newTail = newNode
        curr = head
        num = -9999

        while curr is not None:
            if num != curr.val:
                newPrev = newTail
                newTail.next = ListNode(curr.val)
                num = curr.val
                newTail = newTail.next
            else:
                newTail = newPrev
                newTail.next = None

            curr = curr.next

        return newNode.next