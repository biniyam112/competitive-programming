from typing import List


def numIdenticalPairs( nums: List[int]) -> int:
    output = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                output+=1
    return output
        