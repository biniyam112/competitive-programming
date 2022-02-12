
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    count = len(nums)
    if len(nums) > 1 and nums[-2] == nums[-1]:
        count -=1
    right = 1
    left = 0
    while right < len(nums):
        if nums[right] != nums[left]:
            nums[right],nums[left+1] = nums[left+1],nums[right]
            left+=1
            right+=1
    else:
        while nums[right] == nums[left]:
            if right == len(nums)-1:
                break
        count -=1
        right+=1
        nums[right],nums[left+1] = nums[left+1],nums[right]
        right +=1
        left +=1
    return count

removeDuplicates([1,2,3,3,3,4,5,6,9,9])