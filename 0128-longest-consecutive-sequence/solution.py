class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in numset:
            if num-1 not in numset:
                counter = 1
                current = num
                while current + 1 in numset:
                    counter +=1
                    current +=1
                ans = max(ans, counter)
        return ans
