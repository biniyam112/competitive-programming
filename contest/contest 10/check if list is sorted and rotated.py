from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        def isSorted(lista):
            for i in range(len(lista)-1):
                if lista[i+1] < lista[i]:
                    return False
            return True
        if isSorted(nums):
            return True
        if nums[-1] > nums[0]:
            return False
        revlist = [nums.pop()]
        while len(nums) > 1 and nums[-1] <= revlist[0]:
            revlist.append(nums.pop())
        revlist = revlist[::-1]
        for i in nums:
            revlist.append(i)
        return isSorted(revlist)