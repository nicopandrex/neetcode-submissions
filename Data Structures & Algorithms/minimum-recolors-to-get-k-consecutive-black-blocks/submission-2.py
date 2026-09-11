import math

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        min_count = k
        count = 0
        for right in range(len(blocks)):
            print(left+right)
            print(count)
            if blocks[right] == "W":
                count +=1
            if left + right >= k-1:
                min_count = min(min_count, count)
                if blocks[left] == "W":
                    count -=1 
                left+=1
        return min_count


