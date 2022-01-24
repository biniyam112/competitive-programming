    from typing import List


def minIncrementForUnique( nums: List[int]) -> int:
        nums.sort()
        result  = []
        cost = 0 
        for i in nums:
            if len(result) == 0:
                result.append(i)
            elif result[-1] >= i:
                cost+= (result[-1]+1)-i
                result.append(result[-1]+1)
            else:
                result.append(i)
        return cost
    
minIncrementForUnique([3,2,1,2,1,7])