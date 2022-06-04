from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        presum = [0]
        dic = {}
        dic[0] = 1
        for i in nums:
            presum.append(presum[-1]+i)
            if presum[-1]-k in dic:
                counter += dic[presum[-1]-k]
            if presum[-1] not in dic:
                dic[presum[-1]] = 1
            else:
                dic[presum[-1]] += 1
        return counter