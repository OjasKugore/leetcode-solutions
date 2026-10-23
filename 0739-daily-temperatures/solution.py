class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
