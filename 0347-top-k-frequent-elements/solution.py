from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max = 0
        sorted_keys = sorted(counter, key=counter.get, reverse = True)
        ans = []
        for i in range (k):
            ans.append(sorted_keys[i])
        return ans
            
