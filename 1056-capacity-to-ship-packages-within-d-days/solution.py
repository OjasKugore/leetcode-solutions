class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(capacity: int) -> bool:
            counter = 0
            days_elapsed = 1
            for weight in weights:
                if counter + weight <= capacity:
                    counter += weight
                else:
                    counter = weight
                    days_elapsed += 1
            
            if (days_elapsed > days):
                return False #increase capacity
            else:
                return True 

        low = max(weights)
        high = sum(weights)

        while (low < high):
            mid = low + (high - low) // 2
            if not helper(mid):
                low = mid +1
            else:
                high = mid
        return low
