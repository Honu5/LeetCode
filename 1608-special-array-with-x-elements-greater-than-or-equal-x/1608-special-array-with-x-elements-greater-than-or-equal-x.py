class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        
        for i in range(max(nums)+1):
            cnt=0
            for j in range(len(nums)):
                if nums[j]>=i:
                    cnt+=1
            if i==cnt:
                return i
        return -1
        