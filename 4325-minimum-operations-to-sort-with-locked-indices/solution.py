class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n = len(nums)
        target = [0] * n
        ans = 0
        for i in range (n):
            t = nums[i] - 1
            if t == i:
                continue
            left = min(i, t)
            right = max(i, t)
            for j in range(left, right+1):
                target[j] = 1
            
        for i in range(n):
            if target[i] and locked[i]:
                ans+=1
        if ans > k:
            return -1
        
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j] , nums[j+1]
                    ans+=1
        return ans
