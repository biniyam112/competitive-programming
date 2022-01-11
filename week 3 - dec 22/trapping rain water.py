
from typing import List


def trap(height: List[int]) -> int:
    # decreasing monotonic queue
    monostack = []
    i = 0
    output = 0
    while i < len(height):
        if not monostack or height[i] <= height[monostack[-1]]:
            monostack.append(i)
        else:
            lastvalue = height[monostack[-1]]
            while monostack :
                if height[monostack[-1]] >= height[i]:
                    output += (i-monostack[-1]-1) * min(height[monostack[-1]],height[i])
                    output -= (i-monostack[-1]-1) * lastvalue
                    break
                if height[monostack[-1]] > lastvalue:
                    output += (i-monostack[-1]-1) * min(height[monostack[-1]],height[i])
                    output -= (i-monostack[-1]-1) * lastvalue
                    lastvalue = height[monostack[-1]]
                monostack.pop()
            monostack.append(i)
        i+=1
    return output
                
            
trap([5,4,2,1,2,4,5,7])