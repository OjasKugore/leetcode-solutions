# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        def zigzag(root):
            counter = 0
            q = deque([root])
            ans = []
            while q:
                level = []
                for _ in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
                if counter%2!=0:
                    ans.append(level[::-1])
                else:
                    ans.append(level)

                counter+=1
            return ans
        return zigzag(root)

