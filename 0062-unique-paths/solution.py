from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = int((factorial(m+n-2))/((factorial(m-1)) * factorial(n-1)))
        return ans
