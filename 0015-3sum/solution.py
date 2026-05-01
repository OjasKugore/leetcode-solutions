class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range (n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0: #it means we gotta reduce one of left or right
                    right-=1
                elif total <0: #we gotta increase one of left or right
                    left+=1
                else:
                    ans.append([ nums[i], nums[left], nums[right] ])
                    left+=1
                    right-=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
        return ans 

                   
                
