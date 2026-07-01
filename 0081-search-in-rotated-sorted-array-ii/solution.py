class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        numset=set(nums)
        if target in numset:
            return True
        return False
        
