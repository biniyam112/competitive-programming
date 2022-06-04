from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        i,j = 0,1
        lastvisit = 0
        items,visited = set(),set()
        while i < len(s):
            if i == len(s)-1:
                output.append(1)
                break
            items.add(s[j])
            if s[j] == s[i] or (lastvisit != i and s[j] in visited):
                lastvisit = j
                visited = items.copy()
            if j == len(s)-1:
                output.append(lastvisit-i+1)
                i = lastvisit+1
                j,lastvisit = i,i
                items,visited = set(),set()
            j +=1
        return output