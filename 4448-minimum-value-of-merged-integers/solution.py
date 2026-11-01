class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        arr = []
        temp = ""
        for i in range(0, len(nums)-1, 2):
            temp += str(nums[i]) + str(nums[i+1])
            arr.append(int(temp))
            temp = ""
        return (min(arr))
