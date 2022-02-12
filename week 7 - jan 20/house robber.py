from ast import List


def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    robs = [nums[0],nums[1]]
    i = 2
    while i < len(nums):
        robs.append(max(robs[i-2]+nums[i],robs[i-1]-nums[i-1]+nums[i]))
    i+=1
    return max(robs[len(robs)-2:len(robs)])
    
    
    