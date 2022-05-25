class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter  = 0
        allowed = set(allowed)
        for word in words:
            consistent = True
            for letter in word:
                if letter not in allowed:
                    consistent = False
                    break
            if consistent:
                counter +=1
        return counter
            
            
            