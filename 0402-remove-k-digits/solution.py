class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k == len(num):
            return "0"
        for digit in num:
            while stack and digit < stack[-1] and k >0:
                stack.pop()
                k-=1
            stack.append(digit)
        ans = "".join(stack)
        while k > 0:
            ans = ans[:-1]
            k-=1
        return ans.lstrip('0') or "0"
