class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range (m, len(nums1)):
            nums1[i] = nums2[i-m]
        print(nums1) 

        a, b = 0, m
        while(b!= m+n):
            if (a == b):
                b+=1
                a=0
            else:
                if(nums1[a] > nums1[b]):
                    nums1[a] , nums1[b] = nums1[b], nums1[a]
                a+=1
        
