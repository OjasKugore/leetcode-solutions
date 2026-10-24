class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        ##first we find out subarray maximum
        n = len(nums)
        nxt = [n] * n
        stack = []
        for i, num in enumerate(nums):
            while stack and num >= nums[stack[-1]]:
                j = stack.pop()
                nxt[j] = i
            stack.append(i)
        
        stack = []
        prev = [-1] * n
        for i in range (n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                j = stack.pop()
                prev[j] = i
            stack.append(i)
        sigma_max = 0
        for i in range (n):
            sigma_max += nums[i] * (i - prev[i] ) * (nxt[i] - i)
        
        ##second we find out subarray minimum
        stack = []
        nxt = [n] * n
        prev = [-1] * n
        for i, num in enumerate(nums):
            while stack and num <= nums[stack[-1]]:
                j = stack.pop()
                nxt[j] = i
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                j = stack.pop()
                prev[j] = i
            stack.append(i)
        sigma_min = 0
        for i in range (n):
            sigma_min += nums[i] * (i - prev[i]) * (nxt[i] - i)
        
        return sigma_max - sigma_min
