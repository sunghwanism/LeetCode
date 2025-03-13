# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value_list = []
        while head:
            value_list.append(head.val)
            head = head.next
        return value_list == value_list[::-1]
"""
[Two-Pointer Technique]
 - Use two pointer (slow, fast) to reach the midpoint of the list
 - When fast reaches the end, slow will be at the midpoint
 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head

        # Find the mid node
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr: # -> Finish when curr is finished
            temp = curr.next
            curr.next = prev # Reverse Order
            prev = curr
            curr = temp

        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True
"""


        


