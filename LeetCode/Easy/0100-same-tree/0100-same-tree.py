# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p is None) or (q is None):
            if p == q:
                return True
            else:
                return False
        

        p_result = []
        p_stack = [p]
        q_result = []

        while p_stack:
            node = p_stack.pop()
            p_result.append(node.val)

            if node.right:
                p_stack.append(node.right)

            if node.left:
                p_stack.append(node.left)
            else:
                if node.right:
                    p_result.append("None")

        q_stack = [q]

        while q_stack:
            node = q_stack.pop()
            q_result.append(node.val)

            if node.right:
                q_stack.append(node.right)

            if node.left:
                q_stack.append(node.left)
            else:
                if node.right:
                    q_result.append("None")


        print(p_result, q_result)

        return p_result == q_result



