# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def maxheight(root: TreeNode) -> int:
            nonlocal diameter
            if root is None:
                return 0
            
            left = maxheight(root.left)
            right = maxheight(root.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        maxheight(root)
        return diameter
        

        
