from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     output = []
    #     for i in range(len(nums)):
    #         counter =0 
    #         for j in range(len(nums)):
    #             if nums[i] > nums[j]:
    #                 counter+=1
    #         output.append(counter)
    #     return output
    
    
#     2nd answer
        list2 = nums.copy() 
        #copy a list
        list2.sort()
        newList = []
        for i in nums:
            num = list2.index(i)
            newList.append(num)  
        return newList
        