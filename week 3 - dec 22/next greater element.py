    from typing import List


def nextGreaterElement(  nums1: List[int], nums2: List[int]) -> List[int]:
        memory = {}
        mono_stack = []
        output =[]
        for i in nums2:
            if len(mono_stack) == 0:
                mono_stack.append(i)
                memory[i] = -1
            else:
                print(i)
                while i > mono_stack[-1]:
                    memory[mono_stack[-1]]= i
                    mono_stack.pop()
                    if len(mono_stack) == 0:
                        break
                mono_stack.append(i)
                memory[i] = -1
        print(memory)
        for i in nums1:
            output.append(memory[i])
        return output
    
    
nextGreaterElement([4,1,2],[1,3,4,2])