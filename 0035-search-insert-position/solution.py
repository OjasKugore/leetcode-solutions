class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        ans = -1
        while (low <= high):
            mid = low + (high - low)//2
            if (nums[mid] < target):
                low = mid +1
            elif (nums[mid] > target):
                high = mid - 1
            elif (nums[mid] == target):
                ans = mid
                return ans
                break
        return low 
