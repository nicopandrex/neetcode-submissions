class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # to get the product without the particular value simply divide by the value
        prod = 1
        result = []
        zero_cnt = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=1


        for num in nums:
            if zero_cnt == 1:
                if num:
                    result.append(0)
                else:
                    result.append(prod)
            elif zero_cnt < 1:
                result.append(prod // num)
                
            else:
                result = [0] * len(nums)


            

        return result

        