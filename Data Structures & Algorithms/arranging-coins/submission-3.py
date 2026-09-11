class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0

        r = n
        res = 0
        while l <= r:

            m = (l + r) // 2

            if ((m * (m+1)) // 2) > n:
                r = m - 1
            else:
                l = m +1
                res = max(res, m)

        return res
