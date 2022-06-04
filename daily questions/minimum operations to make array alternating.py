from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        even_count =  len(nums)//2+len(nums)%2
        odd_count = len(nums)//2
        even_dict = {}
        odd_dict = {}
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] in even_dict:
                    even_dict[nums[i]]+= 1
                else:
                    even_dict[nums[i]] = 1
            else:
                if nums[i] in odd_dict:
                    odd_dict[nums[i]]+= 1
                else:
                    odd_dict[nums[i]] = 1
                    
        odd_max_key = nums[1]
        even_max_key = nums[0]
        odd_top = 0
        odd_second = 0
        even_top  = 0
        even_second = 0
        for k,v in odd_dict.items():
            if v >= odd_top:
                odd_max_key = k
                odd_second,odd_top = odd_top,v
            elif v > odd_second:
                odd_second = v
        for k,v in even_dict.items():
            if v >= even_top:
                even_max_key = k
                even_second,even_top = even_top,v
            elif v > even_second:
                even_second = v
        

        if odd_max_key != even_max_key:
            return even_count - even_top + odd_count - odd_top
        return min(even_count - even_top + odd_count - odd_second , even_count - even_second + odd_count - odd_top)

                