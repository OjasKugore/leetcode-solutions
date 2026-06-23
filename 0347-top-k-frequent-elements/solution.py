from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        ans = []
        for _ in range(k):
            update = max(counter, key=counter.get)
            ans.append(update)
            del counter[update] 

        return ans
