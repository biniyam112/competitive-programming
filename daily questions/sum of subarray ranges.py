from typing import List

# using monotonic stack
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        output = 0
        def increasing(value):
            if not increasing_mono or value >= increasing_mono[-1]:
                increasing_mono.append(value)
            else:
                while increasing_mono and increasing_mono[-1] >= value:
                    increasing_mono.pop()
                increasing_mono.append(value)
        def decreasing(value):
            if not decreasing_mono or value <= decreasing_mono[-1]:
                decreasing_mono.append(value)
            else:
                while decreasing_mono and decreasing_mono[-1] <= value:
                    decreasing_mono.pop()
                decreasing_mono.append(value)
        for i in range(len(nums)):
            increasing_mono = []
            decreasing_mono = []
            for j in range(i,len(nums)):
                increasing(nums[j])
                decreasing(nums[j])
                output+=abs(increasing_mono[0]-decreasing_mono[0])
        return output


# using min and max values
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            min_value = nums[i]
            max_value = nums[i]
            for j in range(i,len(nums)):
                min_value = min(min_value,nums[j])
                max_value =  max(max_value,nums[j])
                output+=abs(max_value-min_value)
        return output