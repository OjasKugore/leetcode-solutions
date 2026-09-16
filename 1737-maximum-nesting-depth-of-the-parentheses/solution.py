class Solution:
    def maxDepth(self, s: str) -> int:
        count, maximum = 0, 0
        for i in range(len(s)):
            if (s[i] == "("):
                count += 1
            elif (s[i] == ")"):
                count-=1
            maximum = max(count, maximum)
        
        return maximum
                
