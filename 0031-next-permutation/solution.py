class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if (nums[i] < nums[i+1]):
                pivot = i
                break
        if pivot != -1:
            for i in range (n-1, -1, -1):
                if (nums[i] > nums[pivot]):
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        left = pivot + 1
        right = n-1
        while (left < right):
            nums[left] , nums[right] = nums[right] , nums[left]
            left+=1
            right-=1
