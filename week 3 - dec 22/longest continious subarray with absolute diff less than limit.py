    from typing import Collection, List


def longestSubarray( nums: List[int], limit: int) -> int:
        temp = Collection.deque([])
        right = left = 0
        minvalue = maxvalue = nums[0]
        output = 1
        while right < len(nums):
            temp.append(nums[right])
            minvalue = min(minvalue,nums[right])
            maxvalue = max(maxvalue,nums[right])
            right+=1
            if maxvalue - minvalue <= limit:
                output = max(output,right-left)
            else:
                left+=1
                temp.popleft()
                minvalue = min(temp)
                maxvalue = max(temp)
        return output
    
longestSubarray([8,2,4,7],4)