class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = 1000000000
        ans = 0
        for i in range(n):
            left = i+1
            right  = n-1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                gap = total - target
                if gap>0:
                    #we need to lessen gap
                    right-=1
                elif gap<0:
                    left +=1
                else:
                    return total

                if abs(gap)< closest:
                    closest = abs(gap)
                    ans = total
        return ans
