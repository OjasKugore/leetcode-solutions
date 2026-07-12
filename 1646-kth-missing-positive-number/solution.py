class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        numset = set(arr)
        high = arr[-1] + k
        counter = 0
        for i in range (1, high+1):
            if i not in numset:
                counter +=1
            if counter == k:
                return i

