# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        stack = []
        curr = root
        while curr or stack:
            
            while curr :
                ans.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            
            if stack:
                curr = stack.pop()
        return ans
