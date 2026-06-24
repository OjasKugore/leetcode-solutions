class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        counter, big =1, 0
        for num in numset:
            if (num-1) not in numset:
                i = 1
                while (num+i) in numset:
                    counter+=1
                    i+=1
                big = max(big, counter)
                counter = 1
        return big 
                    
