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

# ? constant space complexity
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(len(nums)-1,-1,-1):
            output.append(output[-1]*nums[i])
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1]
        for i in range(len(nums)):
            if i == 0 :
                temp = nums[i]
                nums[i] = 1 * output[-i-2]
                continue
            temp2 = nums[i]
            nums[i] = temp * output[-i-2]
            temp = temp2
        return nums
            