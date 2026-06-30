from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_keys = sorted(counter, key = counter.get, reverse = True)
        return sorted_keys[0]
