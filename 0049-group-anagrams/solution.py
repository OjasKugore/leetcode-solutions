class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for string in strs:
            key = tuple(sorted(string))
            if (key in counter.keys()):
                counter[key].append(string)
            else:
                counter[key] = [string]
        return list(counter.values())
