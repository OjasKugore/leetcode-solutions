class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = [int(digit) for digit in str(n)]
        if n == sorted(n, reverse = True):
            return -1
        for i in range(len(n) - 1, 0, -1):
            if n[i] > n[i-1]:
                pivot = i-1
                break
        for i in range(len(n) - 1, pivot, -1):
            if (n[i] > n[pivot]):
                n[i] , n[pivot] = n[pivot], n[i]
                break
        n[pivot+1:] = sorted(n[pivot+1:])
        ans = ""
        for digit in n:
            ans += str(digit)
        ans = int(ans)
        return ans if ans <= 2**31-1 else -1

