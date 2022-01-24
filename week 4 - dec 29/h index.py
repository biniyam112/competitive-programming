    from typing import List


def hIndex(  citations: List[int]) -> int:
        citations.sort()
        output = 0
        for i in range(len(citations)+1):
            counter  = 0
            while i > citations[counter]:
                counter +=1
                if counter == len(citations):
                    break
            if len(citations) - counter >= i:
                output = i
        return output
    
    
hIndex([3,0,6,1])