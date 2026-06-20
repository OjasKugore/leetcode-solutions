from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            counter[key].append(word)

        return list(counter.values())
