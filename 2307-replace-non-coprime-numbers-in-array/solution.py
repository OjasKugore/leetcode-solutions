from math import gcd, lcm
class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack =[]
        for num in nums:
                while stack:
                    if gcd(num, stack[-1]) > 1:
                        num = lcm(num, stack[-1])
                        stack.pop()
                    else:
                        break

                stack.append(num)

        return stack
