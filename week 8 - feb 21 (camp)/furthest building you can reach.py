from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
      counter = 0
      ladderList = []
      heapq.heapify(ladderList)
      for i in range(1,len(heights)):
        diff = heights[i] - heights[i-1]
        if diff > 0:
          if ladders > 0:
            heapq.heappush(ladderList,diff)
            ladders-=1
            counter+=1
          else:
            if ladderList:
              minHeight = ladderList[0]
              if diff > minHeight:
                if bricks >= minHeight:
                    heapq.heappop(ladderList)
                    heapq.heappush(ladderList,diff)
                    bricks-=minHeight
                    counter+=1
                else:
                  break
              else:
                if bricks >= diff:
                  bricks-=diff
                  counter+=1
                else:
                    return counter
            # no ladder
            elif bricks >= diff:
              bricks-=diff
              counter+=1
            # no or less bricks and no ladder
            else:
              return counter
        else:
          counter+=1
      return counter
            
          
        
          
          
          