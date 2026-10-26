# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        def recursion(root: TreeNode):
            if root is None:
                return
            recursion(root.left)
            recursion(root.right)
            ans.append(root.val)
        recursion(root)
        return ans
