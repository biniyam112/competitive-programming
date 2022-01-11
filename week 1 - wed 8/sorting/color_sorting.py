from typing import List


def sortColors( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)-1):
        minIndex =i
        for j in range(i,len(nums)):
            if nums[j]< nums[minIndex]:
                minIndex = j
        nums[minIndex],nums[i] = nums[i],nums[minIndex]
    print(nums)
        
    