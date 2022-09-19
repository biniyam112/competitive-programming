cases = int(input())
for _ in range(cases):
    input()
    s = input()
    stack = []
    visited = set()
    i = 0
    j = len(s)-1
    moves = 0
    for i in s:
        if i == '(':
            stack.append('(')
        if i == ')' and not stack or stack[-1] == ')':
            moves += 1
        elif i == ')' and stack[-1] == '(':
            stack.pop()
    print(moves)
