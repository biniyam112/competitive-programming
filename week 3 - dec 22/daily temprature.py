    from typing import List


def dailyTemperatures(  temperatures: List[int]) -> List[int]:
        mon_stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(mon_stack) == 0:
                mon_stack.append(i)
            elif temperatures[i] < temperatures[mon_stack[-1]]:
                mon_stack.append(i)
            else:
                while temperatures[mon_stack[-1]] < temperatures[i]:
                    output[mon_stack[-1]]= i-mon_stack[-1]
                    mon_stack.pop()
                    if len(mon_stack) == 0:
                        break
                mon_stack.append(i)
        return output
    
    
dailyTemperatures([73,74,75,71,69,72,76,73])