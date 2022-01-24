    from typing import List


def validateStackSequences( pushed: List[int], popped: List[int]) -> bool:
        output = True
        mylist = []
        i = 0
        pushed.reverse()
        while len(popped) > i:
            if len(mylist) == 0:
                 mylist.append(pushed.pop())
            if mylist[-1] != popped[i]:
                if len(pushed) == 0:
                    return False
                mylist.append(pushed.pop())
            else:
                mylist.pop()
                i+=1
        return True
    
validateStackSequences([1,2,3,4,5],[4,3,5,1])