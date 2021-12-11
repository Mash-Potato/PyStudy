import sys


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_p = sys.maxsize
#         answer = 0
#         for price in prices:
#             min_p = min(min_p, price)
#             answer = max(answer, price - min_p)
#         return answer

# my code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            min_p = min(min_p, prices[i])
            if prices[i] > min_p:
                answer = max(answer, prices[i]-min_p)
        return answer