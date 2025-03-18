# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        temp = dummyNode

        curr_1, curr_2 = list1, list2

        while curr_1 and curr_2:
            if curr_1.val < curr_2.val :
                temp.next = curr_1
                curr_1 = curr_1.next

            else:
                temp.next = curr_2
                curr_2 = curr_2.next

            temp = temp.next
        
        temp.next = curr_1 if curr_1 else curr_2

        return dummyNode.next

