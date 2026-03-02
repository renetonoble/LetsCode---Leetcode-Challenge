class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc={}
        for i,n in enumerate(nums):
            complement=target-n
            if complement in dc:
                return [dc[complement],i]
                
            
            dc[n]=i    