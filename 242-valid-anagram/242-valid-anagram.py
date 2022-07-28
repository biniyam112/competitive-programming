class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [x for x in s]
        s.sort()
        t = [x for x in t]
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        