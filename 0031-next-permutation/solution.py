class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (nums == sorted(nums, reverse = True)):
            nums.sort()
        else:
            n = len(nums)
            for i  in range (n-2, -1, -1):
                if nums[i] < nums[i+1]:
                    pivot = i
                    break
            for i in range (n-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
            nums[pivot+1:] = nums[pivot+1:][::-1]
