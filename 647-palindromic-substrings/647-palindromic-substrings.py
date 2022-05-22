class Solution:
    def countSubstrings(self, s: str) -> int:
        counter  = 0
        visited = {}
        def ispalindrome(s):
            i = 0
            j = len(s)-1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] in visited and visited[s[i:j]]:
                    counter +=1
                elif s[i:j] not in visited:
                    ispal = ispalindrome(s[i:j])
                    visited[s[i:j]] = ispal
                    if ispal:
                        counter +=1
        return counter
                    
                
        
        