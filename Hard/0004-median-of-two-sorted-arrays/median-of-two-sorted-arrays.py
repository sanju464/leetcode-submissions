class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        x=sorted(num)
        n=len(num)
        y=(n-1)//2
        if n%2!=0:
            return x[y]
        else:
            z=n//2
            med=(x[z]+x[y])/2
            return med


        
