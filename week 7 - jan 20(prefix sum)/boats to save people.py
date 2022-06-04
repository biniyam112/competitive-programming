from typing import List


def numRescueBoats(self, people: List[int], limit: int) -> int:
    people.sort()
    start = 0
    end = len(people)-1
    counter = 0
    while end >= start:
        weightsum = people[start] + people[end]
        if weightsum <= limit :
            start+=1
            end-=1
            counter +=1
        else:
            if people[start] >= people[end]:
                start+=1
            else:
                end-=1
        counter+=1
    return counter