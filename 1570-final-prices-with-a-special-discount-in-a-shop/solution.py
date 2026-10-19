
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        ans = prices.copy()

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                j = stack.pop()
                ans[j] = prices[j] - price

            stack.append(i)

        return ans

