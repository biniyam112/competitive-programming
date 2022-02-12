from ast import List


def moveZeroes(self, nums: List[int]) -> None:
    zero = 0
    nonzero = 1
    while nonzero < len(nums):
        if nums[zero] == 0:
            while nums[nonzero] == 0 :
                nonzero +=1
                if nonzero == len(nums):
                    break
            if nonzero < len(nums):  
                nums[zero],nums[nonzero] = nums[nonzero],nums[zero]
    else:
        zero+=1
        nonzero+=1
    """
    Do not return anything, modify nums in-place instead.
    """
    