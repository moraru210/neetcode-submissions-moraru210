# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(old_tree):
            if old_tree is None:
                return

            left = old_tree.left
            right = old_tree.right
            invert(left)
            invert(right)
            old_tree.right = left
            old_tree.left = right
            return
        
        invert(root)
        return root
        