from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        minweight = 0
        maxweight = len(people)-1
        boats = 0
        while minweight <= maxweight:
            if people[minweight] + people[maxweight] > limit:
                    boats +=1
                    maxweight -=1
            else:
                boats += 1
                minweight +=1
                maxweight -=1
        return boats