class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j,cur = 0,0,0
        while j < len(haystack):
            if haystack[j] != needle[cur]:
                if i == j:
                    i+=1
                    j+=1
                else:
                    i += 1
                    while i < j and haystack[i] != needle[0]:
                        i += 1
                    j = i
                cur = 0
            else:
                j += 1
                cur +=1
            if cur == len(needle):
                return i
        return -1
        