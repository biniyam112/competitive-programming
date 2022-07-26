class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dic = {}
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == 0:
                    dic[str(nums[i])+str(nums[i])+str(nums[k])] = [nums[i],nums[j],nums[k]]
                    j+=1
                elif curSum < 0:
                    j+=1
                else:
                    k-=1
            output = []
            for _,v in dic.items():
                output.append(v)
        return output
                    
        