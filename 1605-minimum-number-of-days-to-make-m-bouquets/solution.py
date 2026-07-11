class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def helper(bloomDay: List[int], day: int, m: int, k: int) -> bool:
            count = 0
            bouquets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    count +=1
                    if count == k:
                        bouquets += 1
                        count = 0 
                else:
                    count = 0
            if bouquets >= m:
                return True
            return False

        if (m*k > len(bloomDay)):
            return -1
        else:
            low = min(bloomDay)
            high = max(bloomDay)
            while (low<high):
                mid = low+(high-low)//2
                if helper(bloomDay, mid, m, k):
                    high = mid
                else:
                    low = mid + 1

        return low

