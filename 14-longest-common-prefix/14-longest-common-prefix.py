class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        minlen = len(strs[0])
        for i in strs:
            minlen = min(minlen,len(i))
        index = 0
        for _ in range(minlen):
            prev = strs[0][index]
            for i in strs:
                if i[index] != prev:
                    return output
            output+=i[index]
            index += 1
        return output
        