from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter({0:1})
        runningsum = 0
        ans = 0
        for i in range (n):
            runningsum += nums[i]
            target = runningsum-k

            if target in count:
                ans+=count[target]
            
            count[runningsum] += 1
        return ans
