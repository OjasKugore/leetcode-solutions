class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*46
        def recursion(n: int, dp: List[int]) -> int:
            
            if n==1:
                return 1
            if n==2:
                return 2

            if dp[n] != -1:
                return dp[n]
            dp[n] = recursion(n-2, dp) + recursion(n-1, dp)
            return dp[n]

        return recursion(n, dp)
