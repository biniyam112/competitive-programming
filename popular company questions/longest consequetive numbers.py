from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            counter = 1
            j = i
            if not i-1 in nums:
                while j+1 in nums:
                    counter+=1
                    j+=1
            longest = max(longest,counter)
        return longest
        