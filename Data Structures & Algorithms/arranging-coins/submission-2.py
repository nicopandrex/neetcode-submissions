class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        j = n
        if n == 1:
            k = 1
        for i in range(1, n, 1):
            
            if j - i >= 0:
                
                k+=1
                j-=i
            else:
                break
        return k
            
