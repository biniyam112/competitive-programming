class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        while i < len(nums):
            j = i+1
            k = len(nums)-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == 0:
                    output.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
                    while k > j and nums[k] == nums[k-1]:
                        k-=1
                    k-=1
                elif curSum < 0:
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
                else:
                    while k > j and nums[k] == nums[k-1]:
                        k-=1
                    k-=1
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return output
                    
        