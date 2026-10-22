class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp, num = "",  ""
                while stack and stack[-1].isalpha():
                    temp += stack.pop()
                temp = temp[::-1]
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                temp = list(num * temp)
                stack+=temp
        return "".join(stack)
