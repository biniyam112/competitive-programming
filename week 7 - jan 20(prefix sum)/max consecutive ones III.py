from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0 :
                if k > 0:
                    k-=1
                    j+=1
                else:
                    output = max(output,j-i)
                    if nums[i] == 0:
                        k+=1
                    i += 1
            else:
                j+=1
        return max(output,j-i)
            
                
            
        