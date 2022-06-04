from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        def getTrips(value):
            counter = 0
            idx = 0
            while idx < len(time) and time[idx] <= value:
                counter += (value//time[idx])
                idx +=1
            return counter
        i = time[0]
        j = min(time) * totalTrips
        best = j
        while i <= j:
            cur = i + (j-i)//2
            trips = getTrips(cur)
            if trips < totalTrips:
                i = cur+1
            else:
                best = cur
                j = cur-1
        return best
            
        
# with out sorting
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 1
        j = min(time) * totalTrips
        best = 0
        while i <= j:
            cur = i + (j-i)//2
            trips = 0
            for k in range(len(time)):
                trips += cur // time[k]
            if trips < totalTrips:
                i = cur+1
            else:
                best = cur
                j = cur-1
        return best
            
        