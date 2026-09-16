from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        table = Counter(s)
        sorted_table = dict(sorted(table.items(), key = lambda item: item[1], reverse = True))
        ans = ""
        for k,v in sorted_table.items():
            ans += k*v 
        return ans
