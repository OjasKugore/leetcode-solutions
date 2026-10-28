class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            
            
            if stack and char == stack[-1][0]:
                stack.append([char, stack[-1][1] + 1])
            else:
                stack.append([char, 1])

            #popping logic
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][0]
        return ans


