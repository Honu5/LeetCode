class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2=set(nums1),set(nums2)
        ans=[]
        for i in n1:
            if i in n2:
                ans.append(i)
        return ans