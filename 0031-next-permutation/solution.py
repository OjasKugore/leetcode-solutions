class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find the breakpoint
        pivot = -1
        n = len(nums)
        for i in range (n-2, -1, -1):
            if (nums[i] < nums[i+1]):
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return
        #swap breakpoint with smallest number on its right
        for i in range (n-1, pivot, -1):
            if (nums[pivot] < nums[i]):
                nums[pivot], nums[i] = nums[i], nums[pivot] 
                break

        #reverse from pivot to end
        nums[pivot + 1:]  = reversed(nums[pivot+1:])
