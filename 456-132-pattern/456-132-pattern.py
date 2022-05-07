# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         # increasing monostack
#         monostack = []
#         i = 0
#         while i < len(nums):
#             if not monostack or monostack[-1] < nums[i]:
#                 monostack.append(nums[i])
#             else:
#                 while monostack and nums[i] < monostack[-1]:
#                     monostack.pop()
#                 if monostack:
#                     return True
#                 monostack.append(nums[i])
#             i += 1
#         return False
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        minVal = nums[0]
        
        for i in range(1,len(nums)):
			# stack should be monotonic decreasing
            while stack and nums[i]>=stack[-1][0]:
                stack.pop()
            
            if stack and nums[i] > stack[-1][1]:
                return True 
            
            stack.append([nums[i],minVal])
			
			# get the minimum value before the current index value
            minVal = min(minVal,nums[i])
            
        return False
