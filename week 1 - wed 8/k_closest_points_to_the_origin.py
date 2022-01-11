from typing import List


def kClosest( points: List[List[int]], k: int) -> List[List[int]]:
    output = []
    distanceList = [0]*len(points)
    for i in range(len(points)):
        distanceList[i] =  points[i][0]**2 + points[i][1]**2
    for i in range(k):
        minIndex = distanceList.index(min(distanceList))
        output.append(points[minIndex])
        points.pop(minIndex)
        distanceList.pop(minIndex)
    
    return output
