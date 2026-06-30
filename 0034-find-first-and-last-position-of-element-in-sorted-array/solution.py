class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary (nums: List[int], target: int, checkleft: bool) -> int:
            n = len(nums)
            low = 0
            high = n-1
            idx = -1
            while (low <= high):
                mid = low + (high-low)//2
                if (nums[mid] < target):
                    low = mid +1
                elif (nums[mid] > target):
                    high = mid - 1
                else:
                    idx = mid
                    if checkleft:
                        high = mid - 1
                    else:
                        low = mid + 1
            return idx
        
        left = binary(nums, target, True)
        right = binary(nums, target, False)
        return [left, right]

