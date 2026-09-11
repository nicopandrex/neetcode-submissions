class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, item in enumerate(nums):
            if target - item in seen:
                return([seen[target-item],i])
            else:
                seen[item] = i
        return ([])
        