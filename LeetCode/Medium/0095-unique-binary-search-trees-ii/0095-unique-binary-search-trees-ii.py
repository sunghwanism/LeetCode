# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def build(start, end):
            trees = []

            if start > end:
                trees.append(None)
                return trees
            
            for root_val in range(start, end+1):
                print(start, root_val-1, "||", root_val+1, end)
                left_trees = build(start, root_val-1)
                right_trees = build(root_val+1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        print(root.val, root.left, root.right)
                        trees.append(root)

            return trees

        return build(1, n)