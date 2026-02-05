# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return 0
            
            left_h = helper(node.left)
            if left_h == -1: return -1

            right_h = helper(node.right)
            if right_h == -1: return -1
            
            if abs(left_h - right_h) > 1:
                return -1

            return max(left_h, right_h) + 1
        
        return helper(root) != -1
