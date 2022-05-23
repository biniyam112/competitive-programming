class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curindex = 0
        for num in nums:
            if num != val:
                nums[curindex] = num
                curindex += 1
        return curindex 
        