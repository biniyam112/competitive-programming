from typing import List
import heapq


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqDict = {}
    for i in nums:
        if  i in freqDict:
            freqDict[i] = freqDict[i] + 1
        else:
            freqDict[i] = 1
    freqList = []
    for key,value in freqDict.items():
        freqList.append((value,key))
    heapq.heapify(freqList)
    for i in range(len(freqDict)-k):
        heapq.heappop(freqList)
    output = []
    for i in freqList:
        output.append(i[1])
    return output
      