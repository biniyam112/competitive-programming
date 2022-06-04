from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mono_stack = []
        i = 0
        profit = 0
        while i < len(prices):
            if not mono_stack or mono_stack[-1] < prices[i]:
                mono_stack.append(prices[i])
            else:
                while mono_stack and mono_stack[-1] > prices[i]:
                    profit = max(profit,abs(mono_stack[0]-mono_stack.pop()))
                mono_stack.append(prices[i])
            i+=1
        return max(profit,mono_stack[-1]-mono_stack[0])
        