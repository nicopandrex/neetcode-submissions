class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[end] + numbers[start] 
            if sum == target:
                return [start+1, end+1]
            elif sum > target:
                end -= 1
            else:
                start+=1
        return []

               