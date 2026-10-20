class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = []
        #first well be finding possible left endpoitns
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        #now come from right side and find possible right endpoints
        for i in range (len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(i - stack.pop() , ans)
            
        return ans
