from typing import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # def removeDuplicates(lista,i):
            # if lista[i]
        lista = [x for x in s]
        duplicates = Counter(s)
        visited = set()
        counter = len(lista)-len(duplicates)
        i = 0
        while counter > 0:
            stack = []
            while duplicates[lista[i]] > 1 :
                stack.append(i)
                i +=1
            while stack:
                current = int(stack.pop())
                if s[current] in visited:
                    lista[current] = ''
                    duplicates[s[current]] = duplicates[s[current]]-1
                    counter -=1
                elif s[current]  > s[i]:
                    lista[current] = ''
                    duplicates[s[current]] = duplicates[s[current]]-1
                    counter -=1
                else:
                    visited.append(s[current])
            i+=1
        return ''.join(lista)
        
        