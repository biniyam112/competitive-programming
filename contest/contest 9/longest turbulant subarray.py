from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def getSign(n,g):
            if arr[n] > arr[g]:
                return 1
            elif arr[n] < arr[g]:
                return -1
            else:
                return 0
        max_ = 1
        if len(arr) == 1:
            return max_
        prev = getSign(0,1)
        if arr[0] != arr[1]:
            items = [arr[0],arr[1]]
        else:
            items = [arr[1]]
        for i in range(1,len(arr)-1):
            if getSign(i,i+1) * prev < 0:
                items.append(arr[i+1])
                prev = getSign(i,i+1)
            else:
                max_ = max(max_,len(items))
                if getSign(i,i+1) == 0:
                    items = [arr[i+1]]
                else:
                    items = [arr[i],arr[i+1]]
                prev = getSign(i,i+1)
        return max(max_,len(items))