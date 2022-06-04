class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        visited = {}
        i = 0
        j = 0
        while j < len(s):
            if s[j] in visited:
                output = max(output,j-i)
                i = max(i,visited[s[j]]+1)
            visited[s[j]] = j
            j+=1
        return max(output,j-i)