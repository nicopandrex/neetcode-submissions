class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = {}

        for i, num in enumerate(nums):
            if num in vals.keys():
                return [vals[num],i]
            else:
                vals[target-num] = i
        return []
            
            
        