class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = ""
        for i in range (1, n+1):
            num += str(i)
        num = list(num)
        for _ in range(k-1):
            pivot = -1
            for i in range (n-2, -1, -1):
                if (num[i] < num[i+1]):
                    pivot = i
                    break

            for i in range (n-1, -1, -1):
                if (num[pivot] < num[i]):
                    num[pivot] , num[i] = num[i] , num[pivot]
                    break
            left, right = pivot+ 1, n-1
            while(left < right):
                num[left] , num[right] = num[right], num[left]
                left+=1
                right-=1
        return "".join(num)
