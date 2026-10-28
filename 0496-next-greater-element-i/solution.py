class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hash = {}
        ans = [-1] * len(nums2)
        for i,num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                j = stack.pop()
                ans[j] = num
            stack.append(i)

            hash[num] = i
        final = []
        for num in nums1:
            final.append(ans[hash[num]])
        return final
        
