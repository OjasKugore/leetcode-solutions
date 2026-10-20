class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [-1] * len(nums)
        for i, num in enumerate (nums):
            while stack and num > nums[stack[-1]]:
                j = stack.pop()
                ans[j] = num
            stack.append(i)
        for j, num in enumerate(nums):
            while stack and num>nums[stack[-1]]:
                k = stack.pop()
                ans[k] = num
        
        
        return (ans)
