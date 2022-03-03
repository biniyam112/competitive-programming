from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers)-1
    while start != end:
        cursum = numbers[start] + numbers[end]
        if cursum == target:
            return [start+1,end+1]
        elif cursum > target :
            end-=1
        else:
            start+=1