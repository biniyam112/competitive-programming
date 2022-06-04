from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        i = 0
        j = 1
        output = len(prices)
        while j < len(prices):
            if prices[j]-prices[j-1] == -1:
                output += j-i
            else:
                i = j
            j+=1
        return output
        