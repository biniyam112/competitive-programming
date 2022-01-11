from typing import List

def PredictTheWinner(nums: List[int]) -> bool:
    start = 0
    end = len(nums)-1
    def recursion(start,end):
        if start == end:
            return nums[start]
        return max(nums[start]-recursion(start+1,end),nums[end]-recursion(start,end-1))
    if recursion(start,end) >= 0:
        print(True)
        return True
    else:
        print(False)
        return False
        

PredictTheWinner([1,2,4,5,4,3,5,324,4,5])