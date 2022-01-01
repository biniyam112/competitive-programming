from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:        
        nums = list(map(str,nums))
        for i in range(len(nums)-1):
            maxIndex = i
            for j in range(i,len(nums)):
                if int(nums[j]+nums[maxIndex]) > int(nums[maxIndex]+nums[j]):
                    maxIndex = j
            nums[i],nums[maxIndex] = nums[maxIndex],nums[i]
        return str(int(''.join(num for num in nums)))
        