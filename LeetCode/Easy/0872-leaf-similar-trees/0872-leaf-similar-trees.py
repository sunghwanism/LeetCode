# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        leaf1 = []
        leaf2 = []

        stack1 = [root1]
        stack2 = [root2]

        while stack1:
            node1 = stack1.pop()
            if node1 is None:
                continue
            elif not node1.left and not node1.right:
                leaf1.append(node1.val)
            stack1.append(node1.right)
            stack1.append(node1.left)
        
        while stack2:
            node2 = stack2.pop()
            if node2 is None:
                continue
            elif not node2.left and not node2.right:
                leaf2.append(node2.val)

            stack2.append(node2.right)
            stack2.append(node2.left)

        return leaf1 == leaf2

        