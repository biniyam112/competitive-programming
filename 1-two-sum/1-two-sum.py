class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[i] = nums[i]
        nums.sort()
        i = 0
        j = len(nums)-1
        output = []
        while i <= j:
            var = nums[i]+nums[j]
            if var == target:
                output = [nums[i],nums[j]]
                break
            elif var < target:
                i +=1
            else:
                j-=1
        temp = []
        for k,v in dic.items():
            if v == output[0]:
                temp.append(k)
            elif v == output[1]:
                temp.append(k)
        temp.sort()
        return temp
            
        