from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        value = len(nums)/3
        freqList = [0] * (max(nums)+1)
        negfreqList = [0] *abs(min(nums))
        for i in nums:
            if i >=0:
                freqList[i] +=1
            else: 
                negfreqList[i] +=1
        for i in range(len(freqList)):
            if freqList[i] > value:
                output.append(i)
        if min (nums)<0:
            for i in range(min(nums),0):
                if negfreqList[i] > value:
                    output.append(i)
        return output
        