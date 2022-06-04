class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                if stack[0] == ')' and locked[i] == '1':
                    return False
                else:
                    stack[0] = '('
            elif locked[i] == '0' and (i < len(s)-1 and locked[i+1] == '1' and s[i] == ')'):
                stack.append('(')
            elif stack[-1] != s[i] or locked[i] == '0':
                stack.pop()
            else:
                stack.append(s[i])
        return not stack

s = Solution()
print(s.canBeValid(s="())()))()(()(((())(()()))))((((()())(())",locked= "10111011000100010010110000001100101"))