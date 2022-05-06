class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1][1] != i:
                stack.append([1,i])
            else:
                stack[-1] = [stack[-1][0]+1,i]
            if stack[-1][0] == k:
                stack.pop()
        output = []
        for i in stack:
            output += [i[1]]*i[0]
        return ''.join(output)
                
        