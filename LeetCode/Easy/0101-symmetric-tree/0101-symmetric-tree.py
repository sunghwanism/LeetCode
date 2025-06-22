# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # **recursive Solution**
        # def symmetric(t1: TreeNode, t2: TreeNode):
        #     if not t1 and not t2:
        #         return True
        #     if not t1 or not t2:
        #         return False
        #     if t1.val != t2.val:
        #         return False
        #     return symmetric(t1.left, t2.right) and symmetric(t1.right, t2.left)

        # return symmetric(root.left, root.right)

        # **Iterative Solution**

        que = [(root.left, root.right)]

        while que:
            node = que[0]
            que = que[1:]

            if not node[0] and not node[1]:
                continue
            
            if not node[0] or not node[1]:
                return False

            if node[0].val != node[1].val:
                return False

            que.append([node[0].left, node[1].right])
            que.append([node[0].right, node[1].left])
        
        return True






                
            