from typing import List


def pivotIndex(self, nums: List[int]) -> int:
    presum = [0]
    for i in nums:
        presum.append(presum[-1]+i)
    for i in range(1,len(presum)):
        if presum[-1] - presum[i] == presum[i-1]:
            return i-1
    return -1