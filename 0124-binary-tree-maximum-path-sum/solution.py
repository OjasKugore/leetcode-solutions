# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        val = -1001
        def dfs(root: TreeNode) -> int:
            nonlocal val
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            val = max(root.val, val, max(0, left) + max(0, right) + root.val)

            
            return root.val + max(0, left, right)
        dfs(root)
        return val
