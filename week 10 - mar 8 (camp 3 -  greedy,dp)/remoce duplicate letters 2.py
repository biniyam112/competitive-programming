from typing import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lista = [x for x in s]
        duplicates = Counter(s)
        counter = len(lista)-len(duplicates)
        i = 0
        stack = []
        while counter > 0:
            while i < len(lista) and duplicates[lista[i]] > 1 and (not stack or lista[stack[-1]] < lista[i]):
                stack.append(i)
                i +=1
            if i >= len(lista):
                break
            print(lista)
            print(stack)
            if s[stack[-1]] == s[i]:
                lista[i] = ''
                duplicates[s[current]] = duplicates[s[current]]-1
                counter -=1
            while stack and s[stack[-1]] > s[i]:
                current = int(stack.pop())
                lista[current] = ''
                duplicates[s[current]] = duplicates[s[current]]-1
                counter -=1
            if duplicates[s[i]] > 1:
                stack.append(i)
            i+=1
        return ''.join(lista)
        
        