
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    maxarea = 0
    monostack = []
    i =0
    while i < len(heights):
        if not monostack or heights[i] >= heights[monostack[-1]]:
            monostack.append(i)
            maxarea = max(maxarea,heights[i])
        else:
            while monostack and heights[i] < heights[monostack[-1]]:
                if len(monostack)>1 :
                    area = (i - monostack[-2]-1) * heights[monostack[-1]]
                else:
                    area = i * heights[monostack[-1]]
                maxarea = max(area,maxarea)
                monostack.pop()
            if monostack:
                area = (i - monostack[-1]) * heights[i]
            else:
                area = (i+1) *  heights[i]
            maxarea =  max(area,maxarea)
            monostack.append(i)
        i+=1
    for i in range(len(monostack)-1,-1,-1):
        if i == 0:
            area = len(heights) * heights[monostack[0]]
        else:
            area = heights[monostack[i]] * (monostack[-1]-monostack[i-1])
        maxarea =  max(maxarea,area)
    return maxarea
        

largestRectangleArea([5,6,7,2,4,9,4,3,2])