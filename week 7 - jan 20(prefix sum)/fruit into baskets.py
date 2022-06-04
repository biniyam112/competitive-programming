from collections import deque
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        output = 0
        baskets = deque()
        i = 0
        j = 0
        while j < len(fruits):
            if not baskets or len(baskets) < 2 and fruits[j] != fruits[baskets[0]]:
                baskets.append(j)
            elif fruits[j] not in [fruits[x] for x in baskets]:
                output = max(output,j-i)
                baskets.popleft()
                baskets.append(j)
                i = baskets[0]
            elif len(baskets) == 2 and fruits[j] != fruits[baskets[1]]:
                baskets.popleft()
                baskets.append(j)
            j+=1
        return max(output,j-i)