from ast import List


def rotate(self, nums: List[int], k: int) -> None:
    def reverse(nums : List[int],start:int,end:int):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
    return nums
    k %= len(nums)
    nums = reverse(nums,0,len(nums)-1)
    nums = reverse(nums,0,k-1)
    nums = reverse(nums,k,len(nums)-1)
    """
    Do not return anything, modify nums in-place instead.
    """
    