from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix = [1]
    suffix = [1]
    for i in range(len(nums)):
        prefix.append(prefix[-1]*nums[i])
        suffix.append(suffix[-1]*nums[len(nums)-i])
    output = []
    for i in range(len(nums)):
        output.append(prefix[i]*suffix[len(nums)-i-1])
    return output