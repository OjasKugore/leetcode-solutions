class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        stack = []
        nxt = [n] * len(arr)
        prev = [-1] * len(arr)
        #next smaller  or equal element
        for i, num in enumerate(arr):
            while stack and num <= arr[stack[-1]]:
                j = stack.pop()
                nxt[j] = i
            stack.append(i)
        
        #prev smaller element
        stack = []
        for i in range (n-1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                prev[j] = i
            stack.append(i)
        
        ans = 0
        for i in range (n):
            ans += arr[i] * (i-prev[i]) * (nxt[i] - i)
        return ans % (10**9 + 7)
