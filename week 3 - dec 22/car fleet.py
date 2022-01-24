    from typing import List


def carFleet( target: int, position: List[int], speed: List[int]) -> int:
        entrytime = [0] * len(position)
        monostack = []
        for i in range(len(position)):
            entrytime[i] = (target - position[i]) / speed[i]
        entrytime = [x for _, x in sorted(zip(position, entrytime),reverse=True, key=lambda pair: pair[0])]
        output = 1
        for i in entrytime:
            if len(monostack) == 0:
                monostack.append(i)
            else:
                if i <= monostack[-1]:
                    monostack.append(i)
                while i > monostack[-1]:
                    monostack.pop()
                    if len(monostack) == 0:
                        monostack.append(i)
                        output+=1
                        break
        return output
    
    
carFleet(12,[10,8,0,5,3],[2,4,1,3])