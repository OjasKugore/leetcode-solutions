class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def helper(divisor: int) -> bool:
            return sum((num + divisor -1) // divisor for num in nums) <= threshold

        low = 1
        high = max(nums)
        while low < high:
            mid = low + (high - low)//2
            if not helper(mid):
                low = mid + 1
            else:
                high = mid
        return low
