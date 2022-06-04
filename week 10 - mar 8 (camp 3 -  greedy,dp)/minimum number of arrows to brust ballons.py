from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        counter = 1
        start = points[0][0]
        end = points[0][1]
        for i in points:
            if i[1] < start  or i[0] > end:
                counter+=1
                start = i[0]
                end = i[1]
            if  i[0] > start:
                start = i[0]
            if i[1] < end:
                end = i[1]
        return counter