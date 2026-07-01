class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums: List[int], target: int) -> int:
            n = len(nums)
            low = 0
            high = n-1
            
            while low <=high:
                mid = low + (high-low)//2
                if (nums[mid] > target):
                    high = mid -1
                elif (nums[mid] < target):
                    low = mid+1
                else:
                    ans = mid
                    return ans
            return -1
                    
        
        n = len(nums)
        r = binary(sorted(nums), nums[0])
        oldpos = binary(sorted(nums), target)
        ans = n -r+oldpos
        if oldpos==-1:
            return -1
        else:
            if ans < n:
                return ans
            else:
                return ans - n
        
        

