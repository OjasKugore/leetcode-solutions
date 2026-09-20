class Solution: 
    def longestPalindrome(self, s: str) -> str:
        def cut_palindrome(left: int, right : int) -> str:
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right +=1
            return s[left + 1: right]    
        
        ans = ""
        for i in range (len(s)):
            #same location
            p1 = cut_palindrome(i, i)
            if len(p1) > len(ans):
                ans = p1
            
            #adjacent
            p2 = cut_palindrome(i, i+1)
            if len(p2) > len(ans):
                ans = p2

        return ans
            
