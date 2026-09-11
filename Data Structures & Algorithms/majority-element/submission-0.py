class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums) // 2
        counts = defaultdict(int)
        count = 0
        canidate = 0
        for num in nums:
            if count == 0:
                canidate = num
            if num == canidate:
                count +=1
            else:
                count -=1
        return canidate
            
            
