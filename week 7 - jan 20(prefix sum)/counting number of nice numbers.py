


from typing import List


def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    counter = 0
    nums = [0 if x%2==0 else 1 for x in nums]
    presum = [0]
    for i in nums:
        presum.append(presum[-1]+i)
    i=j=0
    while j < len(presum):
        if presum[j] < k:
            j+=1
        else:
            if presum[j] - presum[i] == k:
                s = i+1
                l = j+1
                while s < len(presum) and presum[s] == presum[i]:
                    s+=1
                while l < len(presum) and presum[l] == presum[j]:
                    l+=1
                counter += (s-i)*(l-j)
                i = s
                j = l
            elif presum[j]-presum[i] < k:
                j+=1
            else:
                i+=1
    return counter
    
    