class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if (n == 1):
            return nums[n-1]
        if (n%2==0):
            return nums[n//2]
        return nums[n//2 ]
