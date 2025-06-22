# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        stack = [root]

        while stack:
            node = stack.pop(0)
            if not node:
                continue
            node.left, node.right = node.right, node.left

            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return root
            

