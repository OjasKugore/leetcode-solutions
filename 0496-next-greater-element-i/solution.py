class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        lookup = {}
        ans = []
        for num in nums2:
            if not stack or num < stack[-1]:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    lookup[stack[-1]] = num
                    stack.pop()
                stack.append(num)
        for leftover in stack:
            lookup[leftover] = -1
        for num in nums1:
            ans.append(lookup[num])
        return ans
