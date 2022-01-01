from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        if len(intervals )== 1:
            output.append(intervals[0])
            return output
        for i in range(len(intervals)-1):
            minIndex = i
            for j in range(i,len(intervals)):
                if intervals[j][0] < intervals[minIndex][0]:
                    minIndex = j
            intervals[i],intervals[minIndex] = intervals[minIndex],intervals[i]
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0],intervals[i+1][1]= intervals[i][0],max(intervals[i+1][1],intervals[i][1])
            else:
                output.append(intervals[i])
        output.append(intervals[i+1])
                
        return output
        