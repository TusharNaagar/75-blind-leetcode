class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empdict={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in empdict:
                return[empdict[diff],i]
            else:
                empdict[n]=i
        
