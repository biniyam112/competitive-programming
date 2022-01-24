    from typing import List


def maxArea(height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxarea = 0
        while i != j:
            if height[i] > height[j]:
                maxarea = max(maxarea,(j-i)*height[j])
                j-=1
            else:
                maxarea = max(maxarea,(j-i)*height[i])
                i+=1
        return maxarea
    
    
maxArea([4,2,0,3,2,4,3,4])