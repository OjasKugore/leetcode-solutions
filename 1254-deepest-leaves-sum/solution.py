# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        
        def bfs(root: TreeNode) -> int:
            q = deque([root])
            total = 0
            bfs = []
            while q:
                level = []
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)
                bfs.append(level)
            return sum(bfs[-1])
        
        return bfs(root)
