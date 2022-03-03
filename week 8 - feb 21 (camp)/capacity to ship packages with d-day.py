from typing import List


class Solution:
    def possible(self,weights:List[int],capacity:int,days:int):
        counter = 0
        total = 0
        for i in weights:
            if total+i > capacity:
                counter+=1
                total = 0
            total+=i
            if counter > days:
                return False
        if total > 0:
            counter +=1
        return counter <= days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        weightsum = sum(weights)
        i = max(weights)
        j = weightsum
        best = 0
        while i <= j:
            capacity = i+(j-i)//2
            if self.possible(weights,capacity,days):
                best = capacity
                j = capacity-1
            else:
                i = capacity+1
        return best