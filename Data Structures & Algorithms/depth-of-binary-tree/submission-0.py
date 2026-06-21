# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def dfs(node, cur):
            nonlocal max_d
            if node is None:
                return
            
            cur += 1
            max_d = max(cur, max_d)
            dfs(node.left, cur)
            dfs(node.right, cur)
            cur -= 1

        dfs(root, 0)
        return max_d

            
        