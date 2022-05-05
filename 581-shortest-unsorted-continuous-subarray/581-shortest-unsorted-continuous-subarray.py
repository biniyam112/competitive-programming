class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        sor = sorted(nums)
        while i <= j:
            if nums[i] == sor[i]:
                i +=1
            if nums[j] == sor[j]:
                j-=1
            elif nums[i] != sor[i] and nums[j] != sor[j]:
                return j-i+1
        return 0
       
        