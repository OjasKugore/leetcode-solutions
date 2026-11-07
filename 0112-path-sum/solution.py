class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        sums = []

        def dfs(root, curr_sum):
            if not root:
                return

            curr_sum += root.val

            if not root.right and not root.left:
                sums.append(curr_sum)
                return

            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

        dfs(root, 0)

        return targetSum in sums
