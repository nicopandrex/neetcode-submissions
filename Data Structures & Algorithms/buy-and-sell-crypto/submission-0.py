class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxProfit






        # maxProfit = 0
        # l, r = 0,1
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #             profit = prices[r] - prices[l]
        #             maxProfit = max(maxProfit, profit)
        #     else:
        #         l = r
        #     r+=1
        # return maxProfit




        # for i, item in enumerate(prices):
        #     for n in range(i+1, len(prices)):
        #         if prices[n] - item >= profit:
        #             profit = prices[n] - item
        # return profit